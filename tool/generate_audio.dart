// ignore_for_file: avoid_print
import 'dart:io';
import 'dart:math';
import 'dart:typed_data';

void main() {
  final audioDir = Directory('assets/audio');
  if (!audioDir.existsSync()) {
    audioDir.createSync(recursive: true);
  }

  print('Generating professional studio audio assets for MindTrap AI...');

  // =========================================================================
  // 1. tap.wav (45 ms)
  // Crisp, modern, tactile UI micro-pop. Instant attack, woody/bubble body.
  // =========================================================================
  generateWavFile(
    'assets/audio/tap.wav',
    durationSeconds: 0.045,
    sampleRate: 44100,
    isStereo: true,
    generator: (t, dur) {
      final env = exp(-t * 95.0);
      final clickEnv = exp(-t * 300.0);
      // Fast pitch sweep from 580Hz down to 260Hz for that pleasing "pop"
      final freq = 260.0 + 320.0 * exp(-t * 120.0);
      final body = sin(2 * pi * freq * t) + 0.25 * sin(4 * pi * freq * t);
      // Subtle high-frequency click transient for tactile precision
      final click = sin(2 * pi * 3200.0 * t) * clickEnv * 0.35;
      final val = ((body * env * 0.75) + click).clamp(-1.0, 1.0);
      return [val, val];
    },
  );

  // =========================================================================
  // 2. correct.wav (0.65 s)
  // Cheerful, sparkling crystalline chime arpeggio: C6 -> E6 -> G6 -> C7
  // Rich celestial bell harmonics (1x, 2.76x, 5.4x) with natural stereo spread.
  // =========================================================================
  generateWavFile(
    'assets/audio/correct.wav',
    durationSeconds: 0.65,
    sampleRate: 44100,
    isStereo: true,
    generator: (t, dur) {
      double left = 0.0;
      double right = 0.0;

      final notes = [
        {'time': 0.00, 'freq': 1046.50, 'pan': -0.22}, // C6
        {'time': 0.10, 'freq': 1318.51, 'pan': 0.22},  // E6
        {'time': 0.20, 'freq': 1567.98, 'pan': -0.12}, // G6
        {'time': 0.30, 'freq': 2093.00, 'pan': 0.12},  // C7
      ];

      for (final note in notes) {
        final startTime = note['time'] as double;
        final f = note['freq'] as double;
        final pan = note['pan'] as double;

        if (t >= startTime) {
          final dt = t - startTime;
          // Organic bell envelope with soft initial strike and musical tail
          final env = exp(-dt * 7.5);
          // Bell physical overtones
          final tone = sin(2 * pi * f * dt) +
              0.35 * sin(2 * pi * (f * 2.0) * dt) * exp(-dt * 9.0) +
              0.18 * sin(2 * pi * (f * 2.756) * dt) * exp(-dt * 14.0) +
              0.08 * sin(2 * pi * (f * 5.404) * dt) * exp(-dt * 20.0);

          final sample = tone * env * 0.34;
          left += sample * (1.0 - pan);
          right += sample * (1.0 + pan);
        }
      }

      return [left.clamp(-0.95, 0.95), right.clamp(-0.95, 0.95)];
    },
  );

  // =========================================================================
  // 3. wrong.wav (0.35 s)
  // Soft, warm wooden marimba double-tap (220 Hz -> 174 Hz).
  // Informative and polite, never harsh or annoying.
  // =========================================================================
  generateWavFile(
    'assets/audio/wrong.wav',
    durationSeconds: 0.35,
    sampleRate: 44100,
    isStereo: true,
    generator: (t, dur) {
      double sample = 0.0;
      final pulses = [
        {'time': 0.00, 'freq': 220.0}, // A3
        {'time': 0.12, 'freq': 174.61}, // F3
      ];

      for (final p in pulses) {
        final startTime = p['time'] as double;
        final f = p['freq'] as double;
        if (t >= startTime) {
          final dt = t - startTime;
          final env = exp(-dt * 13.0);
          // Warm marimba/wood block body
          final tone = sin(2 * pi * f * dt) +
              0.30 * sin(2 * pi * (f * 3.0) * dt) * exp(-dt * 20.0) +
              0.15 * sin(2 * pi * (f * 4.0) * dt) * exp(-dt * 25.0);
          sample += tone * env * 0.55;
        }
      }

      final out = sample.clamp(-0.95, 0.95);
      return [out, out];
    },
  );

  // =========================================================================
  // 4. coin.wav (0.45 s)
  // Shimmering, crisp gold coin / gem pickup. Dual-tone resonance: B5 -> E6
  // =========================================================================
  generateWavFile(
    'assets/audio/coin.wav',
    durationSeconds: 0.45,
    sampleRate: 44100,
    isStereo: true,
    generator: (t, dur) {
      double left = 0.0;
      double right = 0.0;

      // Note 1: B5 (987.77 Hz)
      final env1 = exp(-t * 12.0);
      final tone1 = (sin(2 * pi * 987.77 * t) +
              0.4 * sin(2 * pi * (987.77 * 2) * t) +
              0.2 * sin(2 * pi * (987.77 * 3.1) * t)) *
          env1 *
          0.38;
      left += tone1 * 1.1;
      right += tone1 * 0.9;

      // Note 2: E6 (1318.51 Hz) slightly delayed
      if (t >= 0.07) {
        final dt = t - 0.07;
        final env2 = exp(-dt * 8.5);
        final tone2 = (sin(2 * pi * 1318.51 * dt) +
                0.45 * sin(2 * pi * (1318.51 * 2) * dt) +
                0.25 * sin(2 * pi * (1318.51 * 4) * dt)) *
            env2 *
            0.50;
        // Sparkle shimmer
        final sparkle = sin(2 * pi * 3951.0 * dt) * exp(-dt * 18.0) * 0.15;
        left += (tone2 + sparkle) * 0.9;
        right += (tone2 + sparkle) * 1.1;
      }

      return [left.clamp(-0.95, 0.95), right.clamp(-0.95, 0.95)];
    },
  );

  // =========================================================================
  // 5. win.wav (2.5 s)
  // Triumphant celebration fanfare: ascending arpeggio into glorious C major
  // chord with sparkling celesta cascades and rich stereo reverb.
  // =========================================================================
  generateWavFile(
    'assets/audio/win.wav',
    durationSeconds: 2.5,
    sampleRate: 44100,
    isStereo: true,
    generator: (t, dur) {
      double left = 0.0;
      double right = 0.0;

      // Stage 1: Ascending herald notes (C5, E5, G5, B5)
      final herald = [
        {'time': 0.00, 'freq': 523.25, 'pan': -0.2}, // C5
        {'time': 0.12, 'freq': 659.25, 'pan': 0.1},  // E5
        {'time': 0.24, 'freq': 783.99, 'pan': -0.1}, // G5
        {'time': 0.36, 'freq': 987.77, 'pan': 0.2},  // B5
      ];

      for (final h in herald) {
        final st = h['time'] as double;
        final f = h['freq'] as double;
        final pan = h['pan'] as double;
        if (t >= st) {
          final dt = t - st;
          final env = exp(-dt * 5.0);
          final tone = (sin(2 * pi * f * dt) + 0.3 * sin(4 * pi * f * dt)) *
              env *
              0.22;
          left += tone * (1.0 - pan);
          right += tone * (1.0 + pan);
        }
      }

      // Stage 2: Grand majestic chord at t = 0.50s (C5, G5, C6, E6, G6)
      if (t >= 0.50) {
        final dt = t - 0.50;
        final chordEnv = exp(-dt * 1.6);
        final freqs = [523.25, 783.99, 1046.50, 1318.51, 1567.98];
        for (int i = 0; i < freqs.length; i++) {
          final f = freqs[i];
          final pan = (i % 2 == 0) ? -0.25 : 0.25;
          final tone = (sin(2 * pi * f * dt) +
                  0.35 * sin(2 * pi * (f * 2) * dt) +
                  0.15 * sin(2 * pi * (f * 3) * dt)) *
              chordEnv *
              0.13;
          left += tone * (1.0 - pan);
          right += tone * (1.0 + pan);
        }

        // Sparkling victory celesta shimmer
        final sparkleFreq = 2093.0 + 400.0 * sin(dt * 12.0);
        final sparkleEnv = exp(-dt * 2.2);
        final spark = sin(2 * pi * sparkleFreq * dt) * sparkleEnv * 0.10;
        left += spark * 1.2;
        right += spark * 0.8;
      }

      return [left.clamp(-0.95, 0.95), right.clamp(-0.95, 0.95)];
    },
  );

  // =========================================================================
  // 6. lose.wav (1.4 s)
  // Gentle, thoughtful music-box motif (G4 -> F4 -> D4 -> C4).
  // Encouraging and soft.
  // =========================================================================
  generateWavFile(
    'assets/audio/lose.wav',
    durationSeconds: 1.4,
    sampleRate: 44100,
    isStereo: true,
    generator: (t, dur) {
      double left = 0.0;
      double right = 0.0;

      final notes = [
        {'time': 0.00, 'freq': 392.00, 'pan': -0.15}, // G4
        {'time': 0.28, 'freq': 349.23, 'pan': 0.15},  // F4
        {'time': 0.56, 'freq': 293.66, 'pan': -0.10}, // D4
        {'time': 0.84, 'freq': 261.63, 'pan': 0.10},  // C4
      ];

      for (final note in notes) {
        final st = note['time'] as double;
        final f = note['freq'] as double;
        final pan = note['pan'] as double;
        if (t >= st) {
          final dt = t - st;
          final env = exp(-dt * 3.8);
          // Soft music box / warm tine tone
          final tone = (sin(2 * pi * f * dt) +
                  0.30 * sin(4 * pi * f * dt) +
                  0.10 * sin(6 * pi * f * dt)) *
              env *
              0.35;
          left += tone * (1.0 - pan);
          right += tone * (1.0 + pan);
        }
      }

      return [left.clamp(-0.95, 0.95), right.clamp(-0.95, 0.95)];
    },
  );

  // =========================================================================
  // 7. bg_music.wav (24.0 s)
  // MindTrap AI Master Ambient Soundtrack
  // Beautiful neo-soul / relaxing puzzle chord progression:
  // Cmaj9 (6s) -> Am9 (6s) -> Fmaj9#11 (6s) -> Gsus4 to G (6s)
  // Layers:
  // - Warm Electric Piano / Rhodes arpeggios
  // - Lush stereo analog pad with slow chorus
  // - Deep warm acoustic upright bass
  // - Sparkling celesta melody
  // - Seamless circular crossfade: mathematically 100% gapless and endless loop!
  // =========================================================================
  generateSeamlessLoopWavFile(
    'assets/audio/bg_music.wav',
    loopDurationSeconds: 24.0,
    crossfadeSeconds: 3.0,
    sampleRate: 44100,
    rawGenerator: (t) {
      double left = 0.0;
      double right = 0.0;

      // 4 chords across 24 seconds = 6 seconds per chord
      // Loop beat: 4 bars of 4 beats = 16 beats total, 1.5s per beat
      final beat = t / 1.5;
      final chordIdx = (t / 6.0).floor() % 4;
      final timeInChord = t % 6.0;

      // Chord definitions [root, 3rd, 5th, 7th, 9th]
      final chordTones = [
        [130.81, 261.63, 329.63, 392.00, 493.88, 587.33], // Cmaj9
        [110.00, 220.00, 261.63, 329.63, 392.00, 493.88], // Am9
        [87.31, 174.61, 261.63, 329.63, 370.00, 440.00],  // Fmaj9#11 (dreamy!)
        [98.00, 196.00, 261.63, 293.66, 392.00, 493.88],  // Gsus4 / G
      ];

      final currentChord = chordTones[chordIdx];
      final bassFreq = currentChord[0];

      // Layer A: Warm Ambient Synth Pad (Stereo chorus, lush and wide)
      final padVoicing = [currentChord[1], currentChord[2], currentChord[3], currentChord[4]];
      for (int i = 0; i < padVoicing.length; i++) {
        final f = padVoicing[i];
        // Slow gentle LFO stereo chorus
        final lfoL = 0.88 + 0.12 * sin(2 * pi * 0.2 * t + i);
        final lfoR = 0.88 + 0.12 * cos(2 * pi * 0.2 * t + i);
        // Slightly detuned oscillators for lush warmth
        final toneL = sin(2 * pi * f * t) + 0.20 * sin(2 * pi * (f * 1.002) * t);
        final toneR = sin(2 * pi * (f * 0.998) * t) + 0.20 * sin(2 * pi * (f * 1.001) * t);
        final padSample = 0.055;
        left += toneL * lfoL * padSample;
        right += toneR * lfoR * padSample;
      }

      // Layer B: Deep Acoustic Sub Bass (Centered, warm and punchy)
      // Plucks on beat 1 and beat 3 of each bar
      final bassBeat = beat % 2.0;
      final bassEnv = exp(-bassBeat * 2.2);
      final bassTone = sin(2 * pi * bassFreq * t) +
          0.35 * sin(4 * pi * bassFreq * t) * exp(-bassBeat * 4.0);
      final bassVal = bassTone * bassEnv * 0.20;
      left += bassVal;
      right += bassVal;

      // Layer C: Electric Piano / Rhodes Arpeggio
      // Plays gentle notes every 0.75s (eighth notes)
      final arpIndex = (t / 0.75).floor();
      final arpTime = t % 0.75;
      final arpNoteIdx = (arpIndex % (currentChord.length - 1)) + 1;
      final arpF = currentChord[arpNoteIdx];
      final arpEnv = exp(-arpTime * 4.5);
      // Rhodes harmonic mix: fundamental + soft 2nd + tine overtone
      final rhodesTone = sin(2 * pi * arpF * arpTime) +
          0.28 * sin(2 * pi * (arpF * 2.0) * arpTime) +
          0.12 * sin(2 * pi * (arpF * 3.0) * arpTime) +
          0.08 * sin(2 * pi * (arpF * 4.0) * arpTime) * exp(-arpTime * 12.0);
      final arpPan = ((arpIndex % 2 == 0) ? -0.28 : 0.28);
      final arpVal = rhodesTone * arpEnv * 0.14;
      left += arpVal * (1.0 - arpPan);
      right += arpVal * (1.0 + arpPan);

      // Layer D: Shimmering Music Box / Celesta Melodic Motif
      // Subtle sparkle phrase in the upper register (notes at bar 1, 2, 3)
      final melodyPattern = [
        {'bar': 0, 'beat': 1.0, 'freq': 1046.50}, // C6
        {'bar': 0, 'beat': 2.5, 'freq': 1174.66}, // D6
        {'bar': 1, 'beat': 0.5, 'freq': 1318.51}, // E6
        {'bar': 1, 'beat': 2.0, 'freq': 987.77},  // B5
        {'bar': 2, 'beat': 1.0, 'freq': 880.00},  // A5
        {'bar': 2, 'beat': 2.5, 'freq': 1046.50}, // C6
        {'bar': 3, 'beat': 1.0, 'freq': 1174.66}, // D6
        {'bar': 3, 'beat': 2.5, 'freq': 987.77},  // B5
      ];

      final currentBar = (t / 6.0).floor() % 4;

      for (final m in melodyPattern) {
        if (m['bar'] == currentBar) {
          final mBeat = m['beat'] as double;
          final mFreq = m['freq'] as double;
          final noteTime = mBeat * 1.5;
          if (timeInChord >= noteTime && timeInChord < noteTime + 2.0) {
            final dt = timeInChord - noteTime;
            final mEnv = exp(-dt * 3.2);
            final mTone = (sin(2 * pi * mFreq * dt) +
                    0.25 * sin(2 * pi * (mFreq * 2.756) * dt) * exp(-dt * 8.0)) *
                mEnv *
                0.09;
            left += mTone * 0.85;
            right += mTone * 1.15;
          }
        }
      }

      return [left.clamp(-0.92, 0.92), right.clamp(-0.92, 0.92)];
    },
  );

  print('All professional audio assets generated successfully!');
}

/// Generates a standard WAV file
void generateWavFile(
  String filePath, {
  required double durationSeconds,
  required int sampleRate,
  required bool isStereo,
  required List<double> Function(double t, double duration) generator,
}) {
  final numSamples = (durationSeconds * sampleRate).toInt();
  final byteData = BytesBuilder();

  final numChannels = isStereo ? 2 : 1;
  final subChunk2Size = numSamples * numChannels * 2;
  final chunkSize = 36 + subChunk2Size;

  byteData.add('RIFF'.codeUnits);
  byteData.add(_int32LE(chunkSize));
  byteData.add('WAVE'.codeUnits);

  byteData.add('fmt '.codeUnits);
  byteData.add(_int32LE(16));
  byteData.add(_int16LE(1)); // PCM
  byteData.add(_int16LE(numChannels));
  byteData.add(_int32LE(sampleRate));
  byteData.add(_int32LE(sampleRate * numChannels * 2));
  byteData.add(_int16LE(numChannels * 2));
  byteData.add(_int16LE(16)); // 16-bit

  byteData.add('data'.codeUnits);
  byteData.add(_int32LE(subChunk2Size));

  for (int i = 0; i < numSamples; i++) {
    final t = i / sampleRate;
    final channels = generator(t, durationSeconds);
    if (isStereo) {
      final leftInt = (channels[0] * 32767).toInt().clamp(-32768, 32767);
      final rightInt = (channels[1] * 32767).toInt().clamp(-32768, 32767);
      byteData.add(_int16LE(leftInt));
      byteData.add(_int16LE(rightInt));
    } else {
      final sampleInt = (channels[0] * 32767).toInt().clamp(-32768, 32767);
      byteData.add(_int16LE(sampleInt));
    }
  }

  final file = File(filePath);
  file.writeAsBytesSync(byteData.toBytes());
  print('-> $filePath (${(file.lengthSync() / 1024).toStringAsFixed(1)} KB)');
}

/// Generates an infinitely seamless looping WAV file using equal-power boundary crossfade.
/// Synthesizes loopDuration + crossfade, then folds the tail seamlessly into the head.
void generateSeamlessLoopWavFile(
  String filePath, {
  required double loopDurationSeconds,
  required double crossfadeSeconds,
  required int sampleRate,
  required List<double> Function(double t) rawGenerator,
}) {
  final loopSamples = (loopDurationSeconds * sampleRate).toInt();
  final xfadeSamples = (crossfadeSeconds * sampleRate).toInt();
  final totalSamples = loopSamples + xfadeSamples;

  // Synthesize raw stream for totalSamples
  final rawLeft = Float64List(totalSamples);
  final rawRight = Float64List(totalSamples);

  for (int i = 0; i < totalSamples; i++) {
    final t = i / sampleRate;
    final s = rawGenerator(t);
    rawLeft[i] = s[0];
    rawRight[i] = s[1];
  }

  // Crossfade: fold tail (loopSamples .. loopSamples + xfadeSamples) into head (0 .. xfadeSamples)
  // using smooth equal-power crossfade curves
  final outLeft = Float64List(loopSamples);
  final outRight = Float64List(loopSamples);

  for (int i = 0; i < loopSamples; i++) {
    if (i < xfadeSamples) {
      final progress = i / xfadeSamples;
      // Equal power curves: cos and sin preserve total RMS energy!
      final angle = progress * (pi / 2.0);
      final gainHead = sin(angle); // 0 -> 1
      final gainTail = cos(angle); // 1 -> 0

      final tailIdx = loopSamples + i;
      outLeft[i] = rawLeft[i] * gainHead + rawLeft[tailIdx] * gainTail;
      outRight[i] = rawRight[i] * gainHead + rawRight[tailIdx] * gainTail;
    } else {
      outLeft[i] = rawLeft[i];
      outRight[i] = rawRight[i];
    }
  }

  // Write out WAV file of exactly loopDurationSeconds
  final byteData = BytesBuilder();
  const numChannels = 2;
  final subChunk2Size = loopSamples * numChannels * 2;
  final chunkSize = 36 + subChunk2Size;

  byteData.add('RIFF'.codeUnits);
  byteData.add(_int32LE(chunkSize));
  byteData.add('WAVE'.codeUnits);

  byteData.add('fmt '.codeUnits);
  byteData.add(_int32LE(16));
  byteData.add(_int16LE(1)); // PCM
  byteData.add(_int16LE(numChannels));
  byteData.add(_int32LE(sampleRate));
  byteData.add(_int32LE(sampleRate * numChannels * 2));
  byteData.add(_int16LE(numChannels * 2));
  byteData.add(_int16LE(16));

  byteData.add('data'.codeUnits);
  byteData.add(_int32LE(subChunk2Size));

  for (int i = 0; i < loopSamples; i++) {
    final l = (outLeft[i] * 32767).toInt().clamp(-32768, 32767);
    final r = (outRight[i] * 32767).toInt().clamp(-32768, 32767);
    byteData.add(_int16LE(l));
    byteData.add(_int16LE(r));
  }

  final file = File(filePath);
  file.writeAsBytesSync(byteData.toBytes());
  print('-> $filePath (Seamless Loop: ${loopDurationSeconds}s, ${(file.lengthSync() / 1024).toStringAsFixed(1)} KB)');
}

List<int> _int16LE(int value) {
  final bd = ByteData(2)..setInt16(0, value, Endian.little);
  return bd.buffer.asUint8List();
}

List<int> _int32LE(int value) {
  final bd = ByteData(4)..setInt32(0, value, Endian.little);
  return bd.buffer.asUint8List();
}
