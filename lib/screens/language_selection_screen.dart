import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../localization/app_language.dart';
import '../localization/language_controller.dart';

class LanguageSelectionScreen extends StatefulWidget {
  final bool isFromSettings;
  final VoidCallback? onLanguageChosen;

  const LanguageSelectionScreen({
    super.key,
    this.isFromSettings = false,
    this.onLanguageChosen,
  });

  @override
  State<LanguageSelectionScreen> createState() => _LanguageSelectionScreenState();
}

class _LanguageSelectionScreenState extends State<LanguageSelectionScreen> {
  late String _selectedCode;
  final TextEditingController _searchController = TextEditingController();
  String _searchQuery = '';

  @override
  void initState() {
    super.initState();
    _selectedCode = LanguageController.instance.currentCode;
    _searchController.addListener(() {
      setState(() {
        _searchQuery = _searchController.text.trim().toLowerCase();
      });
    });
  }

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  void _onLanguageTapped(String code) {
    HapticFeedback.selectionClick();
    setState(() {
      _selectedCode = code;
      AppStrings.currentCode = code;
    });
  }

  Future<void> _applyLanguage() async {
    HapticFeedback.mediumImpact();
    await LanguageController.instance.setLanguage(_selectedCode);
    if (!mounted) return;

    if (widget.onLanguageChosen != null) {
      widget.onLanguageChosen!();
      return;
    }

    if (widget.isFromSettings) {
      Navigator.of(context).pop();
    } else {
      if (Navigator.of(context).canPop()) {
        Navigator.of(context).pop();
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final allLanguages = AppStrings.supportedLanguages;

    return ValueListenableBuilder<String>(
      valueListenable: LanguageController.instance.activeLanguage,
      builder: (context, langCode, _) {
        final filteredLanguages = allLanguages.where((lang) {
          if (_searchQuery.isEmpty) return true;
          return lang.englishName.toLowerCase().contains(_searchQuery) ||
              lang.nativeName.toLowerCase().contains(_searchQuery) ||
              lang.code.toLowerCase().contains(_searchQuery);
        }).toList();

        return Directionality(
          textDirection: LanguageController.instance.directionality,
          child: Scaffold(
            body: Stack(
              children: [
                // 1. Sunny Mountain Scenic Background
                const Positioned.fill(
                  child: Image(
                    image: AssetImage('assets/images/home_background.webp'),
                    fit: BoxFit.cover,
                    alignment: Alignment.center,
                  ),
                ),

                // 2. Soft Bright Subtle Vignette for maximum text legibility
                Positioned.fill(
                  child: DecoratedBox(
                    decoration: BoxDecoration(
                      gradient: LinearGradient(
                        begin: Alignment.topCenter,
                        end: Alignment.bottomCenter,
                        colors: [
                          Colors.white.withAlpha(50),
                          Colors.transparent,
                          Colors.white.withAlpha(90),
                        ],
                        stops: const [0.0, 0.45, 1.0],
                      ),
                    ),
                  ),
                ),

                SafeArea(
                  child: Column(
                    children: [
                      // Top Navigation / Counter Bar
                      Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 8),
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            if (widget.isFromSettings || Navigator.of(context).canPop())
                              Material(
                                color: Colors.white,
                                shape: const CircleBorder(),
                                elevation: 2,
                                shadowColor: const Color(0x332178BA),
                                child: InkWell(
                                  customBorder: const CircleBorder(),
                                  onTap: () => Navigator.of(context).pop(),
                                  child: SizedBox(
                                    width: 38,
                                    height: 38,
                                    child: Icon(
                                      (Directionality.of(context) == TextDirection.rtl)
                                          ? Icons.arrow_forward_rounded
                                          : Icons.arrow_back_rounded,
                                      color: const Color(0xFF244169),
                                      size: 24,
                                    ),
                                  ),
                                ),
                              )
                            else
                              const SizedBox(width: 44),
                            Container(
                              padding: const EdgeInsets.symmetric(
                                horizontal: 16,
                                vertical: 7,
                              ),
                              decoration: BoxDecoration(
                                color: Colors.white.withAlpha(230),
                                borderRadius: BorderRadius.circular(20),
                                border: Border.all(
                                  color: const Color(0xFFBAE6FD),
                                  width: 1.2,
                                ),
                                boxShadow: const [
                                  BoxShadow(
                                    color: Color(0x100284C7),
                                    blurRadius: 8,
                                    offset: Offset(0, 2),
                                  ),
                                ],
                              ),
                              child: Text(
                                '${allLanguages.length} Languages',
                                style: const TextStyle(
                                  color: Color(0xFF0284C7),
                                  fontSize: 12.5,
                                  fontWeight: FontWeight.w900,
                                  letterSpacing: 0.3,
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),

                      // Header Medallion & Titles
                      Padding(
                        padding: const EdgeInsets.symmetric(
                          horizontal: 24,
                          vertical: 6,
                        ),
                        child: Column(
                          children: [
                            Container(
                              width: 68,
                              height: 68,
                              decoration: BoxDecoration(
                                shape: BoxShape.circle,
                                gradient: const LinearGradient(
                                  colors: [Color(0xFF38BDF8), Color(0xFF0284C7)],
                                  begin: Alignment.topLeft,
                                  end: Alignment.bottomRight,
                                ),
                                border: Border.all(
                                  color: Colors.white,
                                  width: 3,
                                ),
                                boxShadow: [
                                  BoxShadow(
                                    color: const Color(0xFF0284C7).withAlpha(100),
                                    blurRadius: 18,
                                    offset: const Offset(0, 5),
                                  ),
                                ],
                              ),
                              child: const Center(
                                child: Icon(
                                  Icons.translate_rounded,
                                  color: Colors.white,
                                  size: 32,
                                ),
                              ),
                            ),
                            const SizedBox(height: 12),
                            Text(
                              tr('choose_language_title'),
                              textAlign: TextAlign.center,
                              style: const TextStyle(
                                color: Color(0xFF0F172A),
                                fontSize: 24,
                                fontWeight: FontWeight.w900,
                                letterSpacing: -0.2,
                              ),
                            ),
                            const SizedBox(height: 5),
                            Text(
                              tr('choose_language_subtitle'),
                              textAlign: TextAlign.center,
                              style: const TextStyle(
                                color: Color(0xFF334155),
                                fontSize: 14,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
                          ],
                        ),
                      ),
                      const SizedBox(height: 10),

                      // Real-time Search Field
                      Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 20),
                        child: Container(
                          decoration: BoxDecoration(
                            color: Colors.white.withAlpha(235),
                            borderRadius: BorderRadius.circular(20),
                            border: Border.all(
                              color: const Color(0xFFBAE6FD),
                              width: 1.5,
                            ),
                            boxShadow: const [
                              BoxShadow(
                                color: Color(0x120284C7),
                                blurRadius: 14,
                                offset: Offset(0, 4),
                              ),
                            ],
                          ),
                          child: TextField(
                            controller: _searchController,
                            style: const TextStyle(
                              color: Color(0xFF0F172A),
                              fontSize: 15,
                              fontWeight: FontWeight.w700,
                            ),
                            decoration: InputDecoration(
                              hintText: tr('search_language'),
                              hintStyle: const TextStyle(
                                color: Color(0xFF94A3B8),
                                fontSize: 14.5,
                                fontWeight: FontWeight.w500,
                              ),
                              prefixIcon: const Icon(
                                Icons.search_rounded,
                                color: Color(0xFF0284C7),
                                size: 22,
                              ),
                              suffixIcon: _searchQuery.isNotEmpty
                                  ? IconButton(
                                      icon: const Icon(
                                        Icons.close_rounded,
                                        color: Color(0xFF64748B),
                                        size: 20,
                                      ),
                                      onPressed: () => _searchController.clear(),
                                    )
                                  : null,
                              border: InputBorder.none,
                              contentPadding: const EdgeInsets.symmetric(
                                horizontal: 16,
                                vertical: 14,
                              ),
                            ),
                          ),
                        ),
                      ),
                      const SizedBox(height: 12),

                      // Languages List or Empty State
                      Expanded(
                        child: filteredLanguages.isEmpty
                            ? Center(
                                child: Column(
                                  mainAxisSize: MainAxisSize.min,
                                  children: [
                                    const Icon(
                                      Icons.search_off_rounded,
                                      color: Color(0xFF0284C7),
                                      size: 48,
                                    ),
                                    const SizedBox(height: 12),
                                    Text(
                                      tr('no_languages_found'),
                                      style: const TextStyle(
                                        color: Color(0xFF475569),
                                        fontSize: 16,
                                        fontWeight: FontWeight.w700,
                                      ),
                                    ),
                                  ],
                                ),
                              )
                            : ListView.builder(
                                padding: const EdgeInsets.symmetric(
                                  horizontal: 20,
                                  vertical: 4,
                                ),
                                itemCount: filteredLanguages.length,
                                itemBuilder: (context, index) {
                                  final lang = filteredLanguages[index];
                                  final isSelected = lang.code == _selectedCode;

                                  return Padding(
                                    padding: const EdgeInsets.only(bottom: 10),
                                    child: Material(
                                      color: Colors.transparent,
                                      borderRadius: BorderRadius.circular(20),
                                      child: InkWell(
                                        onTap: () => _onLanguageTapped(lang.code),
                                        borderRadius: BorderRadius.circular(20),
                                        child: AnimatedContainer(
                                          duration: const Duration(
                                            milliseconds: 180,
                                          ),
                                          padding: const EdgeInsets.symmetric(
                                            horizontal: 18,
                                            vertical: 14,
                                          ),
                                          decoration: BoxDecoration(
                                            borderRadius: BorderRadius.circular(20),
                                            color: isSelected
                                                ? Colors.white.withAlpha(245)
                                                : Colors.white.withAlpha(230),
                                            border: Border.all(
                                              color: isSelected
                                                  ? const Color(0xFF0284C7)
                                                  : Colors.white,
                                              width: isSelected ? 2.0 : 1.5,
                                            ),
                                            boxShadow: isSelected
                                                ? [
                                                    BoxShadow(
                                                      color: const Color(0xFF0284C7).withAlpha(50),
                                                      blurRadius: 14,
                                                      offset: const Offset(0, 4),
                                                    ),
                                                  ]
                                                : const [
                                                    BoxShadow(
                                                      color: Color(0x0C0F172A),
                                                      blurRadius: 10,
                                                      offset: Offset(0, 3),
                                                    ),
                                                  ],
                                          ),
                                          child: Row(
                                            children: [
                                              Text(
                                                lang.flagEmoji,
                                                style: const TextStyle(
                                                  fontSize: 28,
                                                ),
                                              ),
                                              const SizedBox(width: 16),
                                              Expanded(
                                                child: Column(
                                                  crossAxisAlignment:
                                                      CrossAxisAlignment.start,
                                                  children: [
                                                    Text(
                                                      lang.englishName,
                                                      style: TextStyle(
                                                        color: const Color(0xFF0F172A),
                                                        fontSize: 17,
                                                        fontWeight: isSelected
                                                            ? FontWeight.w900
                                                            : FontWeight.w800,
                                                      ),
                                                    ),
                                                    const SizedBox(height: 3),
                                                    Text(
                                                      lang.nativeName,
                                                      style: const TextStyle(
                                                        color: Color(0xFF64748B),
                                                        fontSize: 13,
                                                        fontWeight: FontWeight.w600,
                                                      ),
                                                    ),
                                                  ],
                                                ),
                                              ),
                                              if (isSelected)
                                                Container(
                                                  width: 26,
                                                  height: 26,
                                                  decoration: const BoxDecoration(
                                                    shape: BoxShape.circle,
                                                    color: Color(0xFF0284C7),
                                                  ),
                                                  child: const Icon(
                                                    Icons.check_rounded,
                                                    color: Colors.white,
                                                    size: 16,
                                                  ),
                                                )
                                              else
                                                Container(
                                                  width: 26,
                                                  height: 26,
                                                  decoration: BoxDecoration(
                                                    shape: BoxShape.circle,
                                                    border: Border.all(
                                                      color: const Color(0xFFCBD5E1),
                                                      width: 1.8,
                                                    ),
                                                  ),
                                                ),
                                            ],
                                          ),
                                        ),
                                      ),
                                    ),
                                  );
                                },
                              ),
                      ),

                      // Bottom Action Button ("Continue ->")
                      Padding(
                        padding: const EdgeInsets.fromLTRB(24, 10, 24, 20),
                        child: Container(
                          width: double.infinity,
                          height: 54,
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(22),
                            gradient: const LinearGradient(
                              colors: [
                                Color(0xFF38BDF8),
                                Color(0xFF0284C7),
                              ],
                            ),
                            boxShadow: [
                              BoxShadow(
                                color: const Color(0xFF0284C7).withAlpha(100),
                                blurRadius: 18,
                                offset: const Offset(0, 6),
                              ),
                            ],
                          ),
                          child: ElevatedButton(
                            onPressed: _applyLanguage,
                            style: ElevatedButton.styleFrom(
                              backgroundColor: Colors.transparent,
                              shadowColor: Colors.transparent,
                              shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(22),
                              ),
                            ),
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Text(
                                  tr('continue'),
                                  style: const TextStyle(
                                    color: Colors.white,
                                    fontSize: 17,
                                    fontWeight: FontWeight.w900,
                                    letterSpacing: 0.5,
                                  ),
                                ),
                                const SizedBox(width: 8),
                                const Icon(
                                  Icons.arrow_forward_rounded,
                                  color: Colors.white,
                                  size: 20,
                                ),
                              ],
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }
}
