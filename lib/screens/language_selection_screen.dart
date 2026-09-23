import 'package:flutter/material.dart';
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
    setState(() {
      _selectedCode = code;
      AppStrings.currentCode = code;
    });
  }

  Future<void> _applyLanguage() async {
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
        // Compute inside builder so it re-evaluates whenever language changes
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
                const Positioned.fill(
                  child: Image(
                    image: AssetImage('assets/images/Stage-7.webp'),
                    fit: BoxFit.cover,
                    alignment: Alignment.center,
                  ),
                ),
                Positioned.fill(
                  child: DecoratedBox(
                    decoration: BoxDecoration(
                      gradient: LinearGradient(
                        begin: Alignment.topCenter,
                        end: Alignment.bottomCenter,
                        colors: [
                          Colors.black.withAlpha(50),
                          Colors.transparent,
                          Colors.black.withAlpha(140),
                        ],
                        stops: const [0.0, 0.35, 1.0],
                      ),
                    ),
                  ),
                ),
                SafeArea(
                  child: Column(
                    children: [
                      const SizedBox(height: 8),
                      if (widget.isFromSettings)
                        Padding(
                          padding: const EdgeInsets.symmetric(horizontal: 16),
                          child: Row(
                            children: [
                              IconButton(
                                icon: const Icon(
                                  Icons.arrow_back_ios_new_rounded,
                                  color: Colors.white,
                                ),
                                onPressed: () => Navigator.of(context).pop(),
                              ),
                              const Spacer(),
                              Container(
                                padding: const EdgeInsets.symmetric(
                                  horizontal: 12,
                                  vertical: 4,
                                ),
                                decoration: BoxDecoration(
                                  color: const Color(0x330284C7),
                                  borderRadius: BorderRadius.circular(20),
                                  border: Border.all(
                                    color: const Color(0xFF0284C7),
                                    width: 1,
                                  ),
                                ),
                                child: Text(
                                  '${allLanguages.length} Languages',
                                  style: const TextStyle(
                                    color: Color(0xFFBAE6FD),
                                    fontSize: 12,
                                    fontWeight: FontWeight.w700,
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      Padding(
                        padding: const EdgeInsets.symmetric(
                          horizontal: 24,
                          vertical: 6,
                        ),
                        child: Column(
                          children: [
                            Container(
                              padding: const EdgeInsets.all(12),
                              decoration: BoxDecoration(
                                shape: BoxShape.circle,
                                color: const Color(0x330284C7),
                                border: Border.all(
                                  color: const Color(0xFF0284C7),
                                  width: 2,
                                ),
                              ),
                              child: const Icon(
                                Icons.translate_rounded,
                                color: Colors.white,
                              ),
                            ),
                            const SizedBox(height: 10),
                            Text(
                              tr('choose_language_title'),
                              textAlign: TextAlign.center,
                              style: const TextStyle(
                                color: Colors.white,
                                fontSize: 22,
                                fontWeight: FontWeight.w900,
                                shadows: [
                                  Shadow(
                                    color: Color(0x990284C7),
                                    blurRadius: 16,
                                    offset: Offset(0, 4),
                                  ),
                                ],
                              ),
                            ),
                            const SizedBox(height: 4),
                            Text(
                              tr('choose_language_subtitle'),
                              textAlign: TextAlign.center,
                              style: const TextStyle(
                                color: Color(0xFFC7D2FE),
                                fontSize: 13,
                                fontWeight: FontWeight.w500,
                              ),
                            ),
                          ],
                        ),
                      ),
                      const SizedBox(height: 8),

                      // Real-time Search Field
                      Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 20),
                        child: Container(
                          decoration: BoxDecoration(
                            color: Colors.white.withAlpha(20),
                            borderRadius: BorderRadius.circular(16),
                            border: Border.all(
                              color: const Color(0xFF0284C7).withAlpha(120),
                              width: 1.5,
                            ),
                            boxShadow: const [
                              BoxShadow(
                                color: Color(0x220284C7),
                                blurRadius: 10,
                                offset: Offset(0, 3),
                              ),
                            ],
                          ),
                          child: TextField(
                            controller: _searchController,
                            style: const TextStyle(
                              color: Colors.white,
                              fontSize: 15,
                            ),
                            decoration: InputDecoration(
                              hintText: tr('search_language'),
                              hintStyle: TextStyle(
                                color: Colors.white.withAlpha(120),
                                fontSize: 14,
                              ),
                              prefixIcon: const Icon(
                                Icons.search_rounded,
                                color: Color(0xFF38BDF8),
                                size: 22,
                              ),
                              suffixIcon: _searchQuery.isNotEmpty
                                  ? IconButton(
                                      icon: const Icon(
                                        Icons.close_rounded,
                                        color: Colors.white70,
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
                      const SizedBox(height: 10),

                      // Languages List or Empty State
                      Expanded(
                        child: filteredLanguages.isEmpty
                            ? Center(
                                child: Column(
                                  mainAxisSize: MainAxisSize.min,
                                  children: [
                                    const Icon(
                                      Icons.search_off_rounded,
                                      color: Color(0xFF38BDF8),
                                      size: 48,
                                    ),
                                    const SizedBox(height: 12),
                                    Text(
                                      tr('no_languages_found'),
                                      style: const TextStyle(
                                        color: Colors.white70,
                                        fontSize: 16,
                                        fontWeight: FontWeight.w600,
                                      ),
                                    ),
                                  ],
                                ),
                              )
                            : ListView.builder(
                                padding: const EdgeInsets.symmetric(
                                  horizontal: 20,
                                  vertical: 6,
                                ),
                                itemCount: filteredLanguages.length,
                                itemBuilder: (context, index) {
                                  final lang = filteredLanguages[index];
                                  final isSelected = lang.code == _selectedCode;

                                  return Padding(
                                    padding: const EdgeInsets.only(bottom: 10),
                                    child: Material(
                                      color: Colors.transparent,
                                      borderRadius: BorderRadius.circular(18),
                                      child: InkWell(
                                        onTap: () => _onLanguageTapped(lang.code),
                                        borderRadius: BorderRadius.circular(18),
                                        child: AnimatedContainer(
                                          duration: const Duration(
                                            milliseconds: 200,
                                          ),
                                          padding: const EdgeInsets.symmetric(
                                            horizontal: 18,
                                            vertical: 14,
                                          ),
                                          decoration: BoxDecoration(
                                            borderRadius: BorderRadius.circular(18),
                                            color: isSelected
                                                ? const Color(
                                                    0xFF0369A1,
                                                  ).withAlpha(220)
                                                : Colors.white.withAlpha(25),
                                            border: Border.all(
                                              color: isSelected
                                                  ? const Color(0xFF38BDF8)
                                                  : Colors.white.withAlpha(35),
                                              width: isSelected ? 2.2 : 1.2,
                                            ),
                                            boxShadow: isSelected
                                                ? [
                                                    const BoxShadow(
                                                      color: Color(0x660284C7),
                                                      blurRadius: 14,
                                                      spreadRadius: 1,
                                                      offset: Offset(0, 3),
                                                    ),
                                                  ]
                                                : null,
                                          ),
                                          child: Row(
                                            children: [
                                              Text(
                                                lang.flagEmoji,
                                                style: const TextStyle(
                                                  fontSize: 26,
                                                ),
                                              ),
                                              const SizedBox(width: 16),
                                              Expanded(
                                                child: Column(
                                                  crossAxisAlignment:
                                                      CrossAxisAlignment.start,
                                                  children: [
                                                    Text(
                                                      lang.nativeName,
                                                      style: TextStyle(
                                                        color: Colors.white,
                                                        fontSize: 17,
                                                        fontWeight: isSelected
                                                            ? FontWeight.w900
                                                            : FontWeight.w700,
                                                      ),
                                                    ),
                                                    const SizedBox(height: 2),
                                                    Text(
                                                      lang.englishName,
                                                      style: TextStyle(
                                                        color: isSelected
                                                            ? const Color(
                                                                0xFFBAE6FD,
                                                              )
                                                            : const Color(
                                                                0xFF94A3B8,
                                                              ),
                                                        fontSize: 12,
                                                        fontWeight: FontWeight.w500,
                                                      ),
                                                    ),
                                                  ],
                                                ),
                                              ),
                                              Container(
                                                width: 28,
                                                height: 28,
                                                decoration: BoxDecoration(
                                                  shape: BoxShape.circle,
                                                  color: isSelected
                                                      ? const Color(0xFF22C55E)
                                                      : Colors.white.withAlpha(20),
                                                  border: Border.all(
                                                    color: isSelected
                                                        ? Colors.white
                                                        : Colors.white54,
                                                    width: 1.5,
                                                  ),
                                                ),
                                                child: isSelected
                                                    ? const Icon(
                                                        Icons.check_rounded,
                                                        color: Colors.white,
                                                        size: 18,
                                                      )
                                                    : null,
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

                      // Bottom Action Button
                      Padding(
                        padding: const EdgeInsets.fromLTRB(24, 12, 24, 20),
                        child: SizedBox(
                          width: double.infinity,
                          height: 56,
                          child: ElevatedButton(
                            onPressed: _applyLanguage,
                            style: ElevatedButton.styleFrom(
                              padding: EdgeInsets.zero,
                              shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(20),
                              ),
                              elevation: 8,
                              shadowColor: const Color(0x660284C7),
                            ),
                            child: Ink(
                              decoration: BoxDecoration(
                                gradient: const LinearGradient(
                                  colors: [
                                    Color(0xFF0284C7),
                                    Color(0xFF0369A1),
                                    Color(0xFF075985),
                                  ],
                                ),
                                borderRadius: BorderRadius.circular(20),
                                border: Border.all(
                                  color: const Color(0xFF38BDF8),
                                  width: 1.5,
                                ),
                              ),
                              child: Container(
                                alignment: Alignment.center,
                                child: Row(
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  children: [
                                    Text(
                                      tr('continue'),
                                      style: const TextStyle(
                                        color: Colors.white,
                                        fontSize: 18,
                                        fontWeight: FontWeight.w900,
                                        letterSpacing: 0.5,
                                      ),
                                    ),
                                    const SizedBox(width: 8),
                                    const Icon(
                                      Icons.arrow_forward_rounded,
                                      color: Colors.white,
                                      size: 22,
                                    ),
                                  ],
                                ),
                              ),
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
