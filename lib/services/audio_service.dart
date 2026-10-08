import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';

class AudioService {
  AudioService._();
  static final AudioService instance = AudioService._();

  final AudioPlayer _musicPlayer = AudioPlayer();
  final List<AudioPlayer> _tapPlayers = [
    AudioPlayer(),
    AudioPlayer(),
    AudioPlayer(),
  ];
  int _tapIndex = 0;

  final AudioPlayer _correctPlayer = AudioPlayer();
  final AudioPlayer _wrongPlayer = AudioPlayer();
  final AudioPlayer _winPlayer = AudioPlayer();
  final AudioPlayer _losePlayer = AudioPlayer();
  final AudioPlayer _coinPlayer = AudioPlayer();

  final Map<String, Uint8List> _cachedBytes = {};
  bool _isInitialized = false;
  bool _userEnabledMusic = true;

  static const double _musicVolume = 0.85;
  static const double _tapVolume = 1.0;
  static const double _correctVolume = 1.0;
  static const double _wrongVolume = 0.95;
  static const double _coinVolume = 1.0;
  static const double _winVolume = 1.0;
  static const double _loseVolume = 0.95;

  bool get isMusicIdle => _musicPlayer.state != PlayerState.playing;
  bool get isMusicPlaying => _musicPlayer.state == PlayerState.playing;
  bool get isMusicEnabled => _userEnabledMusic;

  // Dedicated AudioContext for BGM
  static final AudioContext _musicAudioContext = AudioContext(
    android: const AudioContextAndroid(
      isSpeakerphoneOn: false,
      stayAwake: false,
      contentType: AndroidContentType.music,
      usageType: AndroidUsageType.game,
      audioFocus: AndroidAudioFocus.gain,
    ),
    iOS: AudioContextIOS(
      category: AVAudioSessionCategory.ambient,
      options: const {
        AVAudioSessionOptions.mixWithOthers,
      },
    ),
  );

  // Dedicated AudioContext for SFX (mixes cleanly with BGM)
  static final AudioContext _sfxAudioContext = AudioContext(
    android: const AudioContextAndroid(
      isSpeakerphoneOn: false,
      stayAwake: false,
      contentType: AndroidContentType.music,
      usageType: AndroidUsageType.game,
      audioFocus: AndroidAudioFocus.gainTransientMayDuck,
    ),
    iOS: AudioContextIOS(
      category: AVAudioSessionCategory.ambient,
      options: const {
        AVAudioSessionOptions.mixWithOthers,
      },
    ),
  );

  List<AudioPlayer> get _allSfxPlayers => [
        ..._tapPlayers,
        _correctPlayer,
        _wrongPlayer,
        _winPlayer,
        _losePlayer,
        _coinPlayer,
      ];

  Future<void> init() async {
    if (_isInitialized) return;
    try {
      try {
        await AudioPlayer.global.setAudioContext(_sfxAudioContext);
      } catch (e) {
        debugPrint('AudioService global context setup: $e');
      }

      // Music player setup
      try {
        await _musicPlayer.setAudioContext(_musicAudioContext);
        await _musicPlayer.setPlayerMode(PlayerMode.mediaPlayer);
        await _musicPlayer.setReleaseMode(ReleaseMode.loop);
        await _musicPlayer.setVolume(_musicVolume);
      } catch (e) {
        debugPrint('AudioService music player setup: $e');
      }

      // SFX players setup with MediaPlayer mode for absolute reliability
      for (final player in _allSfxPlayers) {
        try {
          await player.setAudioContext(_sfxAudioContext);
          await player.setPlayerMode(PlayerMode.mediaPlayer);
          await player.setReleaseMode(ReleaseMode.stop);
        } catch (_) {}
      }

      // Pre-load audio bytes into memory to eliminate I/O lag and path issues
      const soundNames = ['bg_music', 'tap', 'correct', 'wrong', 'win', 'lose', 'coin'];
      for (final name in soundNames) {
        try {
          final data = await rootBundle.load('assets/audio/$name.wav');
          _cachedBytes[name] = data.buffer.asUint8List();
        } catch (e) {
          debugPrint('AudioService preload failed for $name: $e');
        }
      }

      // BGM Loop boundary retrigger safeguard
      _musicPlayer.onPlayerComplete.listen((_) async {
        if (!_userEnabledMusic) return;
        try {
          await _musicPlayer.seek(Duration.zero);
          await _musicPlayer.resume();
        } catch (_) {
          await _playMusicSource();
        }
      });

      _musicPlayer.onPlayerStateChanged.listen((state) {
        if (_userEnabledMusic &&
            (state == PlayerState.completed || state == PlayerState.stopped)) {
          _playMusicSource();
        }
      });

      _isInitialized = true;
      debugPrint('AudioService initialized successfully with cached audio streams');
    } catch (e) {
      debugPrint('AudioService init note: $e');
    }
  }

  /// Start or resume background music if music is enabled
  Future<void> startBackgroundMusic({required bool isMusicEnabled}) async {
    _userEnabledMusic = isMusicEnabled;
    if (!isMusicEnabled) {
      await pauseBackgroundMusic();
      return;
    }

    try {
      if (!_isInitialized) {
        await init();
      }

      if (_musicPlayer.state == PlayerState.playing) {
        return;
      }

      if (_musicPlayer.state == PlayerState.paused) {
        await _musicPlayer.resume();
        return;
      }

      await _playMusicSource();
    } catch (e) {
      debugPrint('AudioService BGM play note: $e');
      await _playMusicBytesFallback();
    }
  }

  Future<void> _playMusicSource() async {
    if (!_userEnabledMusic) return;
    try {
      await _musicPlayer.setReleaseMode(ReleaseMode.loop);
      await _musicPlayer.setVolume(_musicVolume);
      final bgBytes = _cachedBytes['bg_music'];
      if (bgBytes != null) {
        await _musicPlayer.play(BytesSource(bgBytes), volume: _musicVolume);
      } else {
        await _musicPlayer.play(AssetSource('audio/bg_music.wav'), volume: _musicVolume);
      }
      debugPrint('AudioService: started BGM playback');
    } catch (e) {
      debugPrint('AudioService _playMusicSource error: $e, trying fallback...');
      await _playMusicBytesFallback();
    }
  }

  Future<void> _playMusicBytesFallback() async {
    if (!_userEnabledMusic) return;
    try {
      final byteData = await rootBundle.load('assets/audio/bg_music.wav');
      final bytes = byteData.buffer.asUint8List();
      await _musicPlayer.setReleaseMode(ReleaseMode.loop);
      await _musicPlayer.setVolume(_musicVolume);
      await _musicPlayer.play(BytesSource(bytes), volume: _musicVolume);
      debugPrint('AudioService: started BGM playback from bytes fallback');
    } catch (err) {
      debugPrint('AudioService _playMusicBytesFallback note: $err');
    }
  }

  /// Pause background music
  Future<void> pauseBackgroundMusic() async {
    try {
      if (_musicPlayer.state == PlayerState.playing) {
        await _musicPlayer.pause();
        debugPrint('AudioService: paused BGM');
      }
    } catch (e) {
      debugPrint('AudioService BGM pause note: $e');
    }
  }

  /// Resume background music if enabled
  Future<void> resumeBackgroundMusic({required bool isMusicEnabled}) async {
    _userEnabledMusic = isMusicEnabled;
    if (isMusicEnabled) {
      await startBackgroundMusic(isMusicEnabled: true);
    }
  }

  /// Stop background music completely
  Future<void> stopBackgroundMusic() async {
    _userEnabledMusic = false;
    try {
      await _musicPlayer.stop();
      debugPrint('AudioService: stopped BGM');
    } catch (e) {
      debugPrint('AudioService BGM stop note: $e');
    }
  }

  /// Play UI tap / click sound with round-robin player pool for rapid taps
  Future<void> playTap({required bool isSoundEnabled}) async {
    if (!isSoundEnabled) return;
    final player = _tapPlayers[_tapIndex % _tapPlayers.length];
    _tapIndex++;
    await _playSfx(player, 'tap', _tapVolume);
  }

  /// Play UI click sound convenience method
  Future<void> playClick({bool? isSoundEnabled}) async {
    await playTap(isSoundEnabled: isSoundEnabled ?? true);
  }

  /// Play correct answer chime
  Future<void> playCorrect({required bool isSoundEnabled}) async {
    if (!isSoundEnabled) return;
    await _playSfx(_correctPlayer, 'correct', _correctVolume);
  }

  /// Play wrong answer sound
  Future<void> playWrong({required bool isSoundEnabled}) async {
    if (!isSoundEnabled) return;
    await _playSfx(_wrongPlayer, 'wrong', _wrongVolume);
  }

  /// Play celebration/win fanfare
  Future<void> playWin({required bool isSoundEnabled}) async {
    if (!isSoundEnabled) return;
    await _playSfx(_winPlayer, 'win', _winVolume);
  }

  /// Play level lose / game over sound
  Future<void> playLose({required bool isSoundEnabled}) async {
    if (!isSoundEnabled) return;
    await _playSfx(_losePlayer, 'lose', _loseVolume);
  }

  /// Play coin/gem pickup sound
  Future<void> playCoin({required bool isSoundEnabled}) async {
    if (!isSoundEnabled) return;
    await _playSfx(_coinPlayer, 'coin', _coinVolume);
  }

  Future<void> _playSfx(
    AudioPlayer player,
    String soundName,
    double volume,
  ) async {
    try {
      if (!_isInitialized) {
        await init();
      }
      await player.setVolume(volume);
      final bytes = _cachedBytes[soundName];
      if (bytes != null) {
        await player.stop();
        await player.play(BytesSource(bytes), volume: volume);
      } else {
        await player.stop();
        await player.play(AssetSource('audio/$soundName.wav'), volume: volume);
      }
    } catch (e) {
      debugPrint('AudioService SFX play error ($soundName): $e, trying asset fallback...');
      try {
        await player.stop();
        await player.play(AssetSource('audio/$soundName.wav'), volume: volume);
      } catch (err) {
        debugPrint('AudioService SFX Asset fallback error ($soundName): $err');
      }
    }
  }

  void dispose() {
    _musicPlayer.dispose();
    for (final player in _allSfxPlayers) {
      player.dispose();
    }
  }
}
