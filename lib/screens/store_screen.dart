import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../localization/app_language.dart';
import '../localization/language_controller.dart';
import '../main.dart';
import '../widgets/professional_game_icons.dart';

class StorePack {
  final String id;
  final String title;
  final int amount;
  final int bonus;
  final double usdPrice;
  final int pkrPrice;
  final String? tag;
  final List<Color> gradientColors;
  final String imageAsset;
  final bool isDiamonds;

  const StorePack({
    required this.id,
    required this.title,
    required this.amount,
    this.bonus = 0,
    required this.usdPrice,
    required this.pkrPrice,
    this.tag,
    required this.gradientColors,
    required this.imageAsset,
    this.isDiamonds = true,
  });

  int get totalAmount => amount + bonus;
}

class StoreScreen extends StatefulWidget {
  final int initialTabIndex; // 0: Diamonds, 1: Coins, 2: Hints

  const StoreScreen({
    super.key,
    this.initialTabIndex = 0,
  });

  @override
  State<StoreScreen> createState() => _StoreScreenState();
}

class _StoreScreenState extends State<StoreScreen> with SingleTickerProviderStateMixin {
  late TabController _tabController;

  static const List<StorePack> diamondPacks = [
    StorePack(
      id: 'gem_100',
      title: 'Starter Pack',
      amount: 100,
      bonus: 0,
      usdPrice: 0.99,
      pkrPrice: 280,
      tag: 'STARTER',
      gradientColors: [Color(0xFF38BDF8), Color(0xFF2563EB)],
      imageAsset: 'assets/images/gem.webp',
      isDiamonds: true,
    ),
    StorePack(
      id: 'gem_350',
      title: 'Adventurer Pack',
      amount: 300,
      bonus: 50,
      usdPrice: 2.99,
      pkrPrice: 840,
      tag: 'POPULAR',
      gradientColors: [Color(0xFF0EA5E9), Color(0xFF0369A1)],
      imageAsset: 'assets/images/gem.webp',
      isDiamonds: true,
    ),
    StorePack(
      id: 'gem_800',
      title: 'Master Pack',
      amount: 700,
      bonus: 100,
      usdPrice: 6.99,
      pkrPrice: 1950,
      tag: 'HOT',
      gradientColors: [Color(0xFFEC4899), Color(0xFFBE185D)],
      imageAsset: 'assets/images/gem.webp',
      isDiamonds: true,
    ),
    StorePack(
      id: 'gem_2000',
      title: 'Champion Vault',
      amount: 1700,
      bonus: 300,
      usdPrice: 14.99,
      pkrPrice: 4200,
      tag: 'BEST VALUE',
      gradientColors: [Color(0xFFF59E0B), Color(0xFFD97706)],
      imageAsset: 'assets/images/gem.webp',
      isDiamonds: true,
    ),
    StorePack(
      id: 'gem_5000',
      title: 'Imperial Treasury',
      amount: 4000,
      bonus: 1000,
      usdPrice: 34.99,
      pkrPrice: 9800,
      tag: 'ULTIMATE',
      gradientColors: [Color(0xFF10B981), Color(0xFF047857)],
      imageAsset: 'assets/images/gem.webp',
      isDiamonds: true,
    ),
  ];

  static const List<StorePack> coinPacks = [
    StorePack(
      id: 'coin_1000',
      title: 'Coin Pouch',
      amount: 1000,
      bonus: 0,
      usdPrice: 0.99,
      pkrPrice: 280,
      tag: 'STARTER',
      gradientColors: [Color(0xFFFBBF24), Color(0xFFD97706)],
      imageAsset: 'assets/images/coin.webp',
      isDiamonds: false,
    ),
    StorePack(
      id: 'coin_5000',
      title: 'Coin Chest',
      amount: 4500,
      bonus: 500,
      usdPrice: 3.99,
      pkrPrice: 1120,
      tag: 'POPULAR',
      gradientColors: [Color(0xFFF59E0B), Color(0xFFB45309)],
      imageAsset: 'assets/images/coin.webp',
      isDiamonds: false,
    ),
    StorePack(
      id: 'coin_15000',
      title: 'Coin Vault',
      amount: 12000,
      bonus: 3000,
      usdPrice: 9.99,
      pkrPrice: 2800,
      tag: 'BEST VALUE',
      gradientColors: [Color(0xFFEAB308), Color(0xFFCA8A04)],
      imageAsset: 'assets/images/coin.webp',
      isDiamonds: false,
    ),
  ];

  @override
  void initState() {
    super.initState();
    _tabController = TabController(
      length: 3,
      vsync: this,
      initialIndex: widget.initialTabIndex.clamp(0, 2),
    );
    _tabController.addListener(() {
      if (mounted) setState(() {});
    });
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  void _openCheckoutSheet(StorePack pack) {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (ctx) => _CheckoutModal(
        pack: pack,
        onSuccess: (amount, isDiamonds) async {
          if (isDiamonds) {
            await GameStorage.addDiamonds(amount);
          } else {
            await GameStorage.addCoins(amount);
          }
          if (mounted) {
            playCoinSound();
            setState(() {});
            _showSuccessDialog(amount, isDiamonds);
          }
        },
      ),
    );
  }

  void _showSuccessDialog(int amount, bool isDiamonds) {
    showDialog(
      context: context,
      barrierColor: Colors.black.withAlpha(90),
      builder: (ctx) => Dialog(
        backgroundColor: Colors.transparent,
        child: Container(
          padding: const EdgeInsets.all(26),
          constraints: const BoxConstraints(maxWidth: 360),
          decoration: BoxDecoration(
            gradient: const LinearGradient(
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
              colors: [
                Color(0xFFFFFFFF),
                Color(0xFFF8FAFC),
                Color(0xFFF1F5F9),
              ],
            ),
            borderRadius: BorderRadius.circular(28),
            border: Border.all(
              color: Colors.white,
              width: 2.2,
            ),
            boxShadow: [
              BoxShadow(
                color: (isDiamonds ? const Color(0xFF0284C7) : const Color(0xFFD97706)).withAlpha(45),
                blurRadius: 36,
                spreadRadius: 2,
                offset: const Offset(0, 10),
              ),
              BoxShadow(
                color: const Color(0xFF0F172A).withAlpha(20),
                blurRadius: 20,
                offset: const Offset(0, 4),
              ),
            ],
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Container(
                width: 80,
                height: 80,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  gradient: RadialGradient(
                    colors: isDiamonds
                        ? [const Color(0xFF38BDF8), const Color(0xFF0284C7)]
                        : [const Color(0xFFFFE066), const Color(0xFFF59E0B)],
                  ),
                  border: Border.all(color: Colors.white, width: 3),
                  boxShadow: [
                    BoxShadow(
                      color: (isDiamonds ? const Color(0xFF0284C7) : const Color(0xFFF59E0B)).withAlpha(90),
                      blurRadius: 20,
                      offset: const Offset(0, 6),
                    ),
                  ],
                ),
                child: Center(
                  child: Image.asset(
                    isDiamonds ? 'assets/images/gem.webp' : 'assets/images/coin.webp',
                    width: 50,
                    height: 50,
                  ),
                ),
              ),
              const SizedBox(height: 18),
              Text(
                tr('purchase_successful'),
                textAlign: TextAlign.center,
                style: const TextStyle(
                  color: Color(0xFF0F172A),
                  fontSize: 22,
                  fontWeight: FontWeight.w900,
                ),
              ),
              const SizedBox(height: 8),
              Text(
                '+$amount ${isDiamonds ? tr('gems') : tr('coins')}',
                style: TextStyle(
                  color: isDiamonds ? const Color(0xFF0284C7) : const Color(0xFFD97706),
                  fontSize: 26,
                  fontWeight: FontWeight.w900,
                ),
              ),
              const SizedBox(height: 6),
              Text(
                isDiamonds ? tr('diamonds_added') : tr('coins_added'),
                textAlign: TextAlign.center,
                style: const TextStyle(
                  color: Color(0xFF475569),
                  fontSize: 14,
                  fontWeight: FontWeight.w600,
                ),
              ),
              const SizedBox(height: 24),
              Container(
                width: double.infinity,
                height: 48,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(16),
                  gradient: LinearGradient(
                    colors: isDiamonds
                        ? [const Color(0xFF38BDF8), const Color(0xFF0284C7)]
                        : [const Color(0xFFFFB703), const Color(0xFFFB8500)],
                  ),
                  boxShadow: [
                    BoxShadow(
                      color: (isDiamonds ? const Color(0xFF0284C7) : const Color(0xFFFB8500)).withAlpha(80),
                      blurRadius: 16,
                      offset: const Offset(0, 5),
                    ),
                  ],
                ),
                child: ElevatedButton(
                  onPressed: () => Navigator.of(ctx).pop(),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.transparent,
                    shadowColor: Colors.transparent,
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                  ),
                  child: const Text(
                    'AWESOME',
                    style: TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.w900,
                      letterSpacing: 1.2,
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Future<void> _handleBuyHints({
    required int count,
    required int price,
    required bool useGems,
  }) async {
    final success = await GameStorage.buyHints(
      hintCount: count,
      price: price,
      useGems: useGems,
    );
    if (!mounted) return;
    if (success) {
      playWinSound();
      triggerSuccessFeedback();
      showGameNotification(
        context: context,
        message: '$count ${tr('purchase_success')}',
        icon: Icons.check_circle_rounded,
        accentColor: const Color(0xFF16A947),
        iconColor: const Color(0xFF4ADE80),
      );
      setState(() {});
    } else {
      triggerHeavyFeedback();
      showGameNotification(
        context: context,
        message: useGems ? tr('not_enough_gems') : tr('not_enough_coins'),
        icon: Icons.error_rounded,
        accentColor: const Color(0xFFE53935),
        iconColor: const Color(0xFFFCA5A5),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final safePadding = MediaQuery.paddingOf(context);

    return ValueListenableBuilder<String>(
      valueListenable: LanguageController.instance.activeLanguage,
      builder: (context, langCode, _) {
        return Scaffold(
          backgroundColor: const Color(0xFF0A0E17),
          body: Stack(
            children: [
              // 1. Professional Mountain Lake Scenery Backdrop (Stage-7) - 100% Crystal Clear
              const Positioned.fill(
                child: Image(
                  image: AssetImage('assets/images/Stage-7.webp'),
                  fit: BoxFit.cover,
                  alignment: Alignment.center,
                ),
              ),

              // 2. Crystal-Clear Natural Vignette (NO purple, 100% clear scenery)
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

              // 3. Main Content
              SafeArea(
                child: Column(
                  children: [
                    // Top App Bar
                    Padding(
                      padding: const EdgeInsets.fromLTRB(16, 10, 16, 8),
                      child: Row(
                        children: [
                          _buildCircleButton(
                            icon: Icons.arrow_back_rounded,
                            onPressed: () => Navigator.of(context).maybePop(),
                          ),
                          const Spacer(),
                          // Currency Row
                          _buildCurrencyDisplay(),
                          const Spacer(),
                          const SizedBox(width: 44), // balance spacing
                        ],
                      ),
                    ),

                    // Header Title & Tagline
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 6),
                      child: Column(
                        children: [
                          Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Container(
                                padding: const EdgeInsets.all(6),
                                decoration: BoxDecoration(
                                  shape: BoxShape.circle,
                                  color: Colors.white.withAlpha(20),
                                ),
                                child: Image.asset(
                                  'assets/images/gem.webp',
                                  width: 24,
                                  height: 24,
                                ),
                              ),
                              const SizedBox(width: 8),
                              Text(
                                tr('store'),
                                style: const TextStyle(
                                  color: Colors.white,
                                  fontSize: 24,
                                  fontWeight: FontWeight.w900,
                                  letterSpacing: 2.0,
                                  shadows: [
                                    Shadow(color: Colors.black, blurRadius: 10, offset: Offset(0, 2)),
                                  ],
                                ),
                              ),
                            ],
                          ),
                          const SizedBox(height: 4),
                          Text(
                            tr('hint_pack_subtitle'),
                            textAlign: TextAlign.center,
                            style: const TextStyle(
                              color: Colors.white70,
                              fontSize: 12,
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                        ],
                      ),
                    ),

                    const SizedBox(height: 8),

                    // Store Tabs
                    Container(
                      margin: const EdgeInsets.symmetric(horizontal: 20),
                      padding: const EdgeInsets.all(4),
                      decoration: BoxDecoration(
                        color: Colors.black.withAlpha(120),
                        borderRadius: BorderRadius.circular(18),
                        border: Border.all(color: Colors.white.withAlpha(25)),
                      ),
                      child: TabBar(
                        controller: _tabController,
                        indicatorSize: TabBarIndicatorSize.tab,
                        dividerColor: Colors.transparent,
                        indicator: BoxDecoration(
                          gradient: LinearGradient(
                            colors: _tabController.index == 0
                                ? const [Color(0xFF38BDF8), Color(0xFF2563EB)] // Diamonds
                                : (_tabController.index == 1
                                    ? const [Color(0xFFFBBF24), Color(0xFFD97706)] // Coins
                                    : const [Color(0xFFFDE047), Color(0xFFCA8A04)]), // Hints
                          ),
                          borderRadius: BorderRadius.circular(14),
                          boxShadow: [
                            BoxShadow(
                              color: (_tabController.index == 0
                                      ? const Color(0xFF38BDF8)
                                      : (_tabController.index == 1
                                          ? const Color(0xFFF59E0B)
                                          : const Color(0xFFEAB308)))
                                  .withAlpha(140),
                              blurRadius: 12,
                              offset: const Offset(0, 2),
                            ),
                          ],
                        ),
                        labelColor: Colors.white,
                        unselectedLabelColor: Colors.white60,
                        labelStyle: const TextStyle(fontSize: 12, fontWeight: FontWeight.w900, letterSpacing: 0.5),
                        tabs: [
                          Tab(
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Image.asset('assets/images/gem.webp', width: 16, height: 16),
                                const SizedBox(width: 6),
                                Text(tr('gems')),
                              ],
                            ),
                          ),
                          Tab(
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Image.asset('assets/images/coin.webp', width: 16, height: 16),
                                const SizedBox(width: 6),
                                Text(tr('coins')),
                              ],
                            ),
                          ),
                          Tab(
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Image.asset('assets/images/hint-icon.webp', width: 16, height: 16),
                                const SizedBox(width: 6),
                                Text(tr('hints')),
                              ],
                            ),
                          ),
                        ],
                      ),
                    ),

                    const SizedBox(height: 12),

                    // Tab Views
                    Expanded(
                      child: TabBarView(
                        controller: _tabController,
                        children: [
                          // 1. Diamonds Tab
                          _buildPacksList(diamondPacks, isDiamonds: true, safePadding: safePadding),

                          // 2. Coins Tab
                          _buildPacksList(coinPacks, isDiamonds: false, safePadding: safePadding),

                          // 3. Hints Tab
                          _buildHintsTab(safePadding),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        );
      },
    );
  }

  Widget _buildCurrencyDisplay() {
    return ValueListenableBuilder<int>(
      valueListenable: GameStorage.currencyNotifier,
      builder: (context, _, child) {
        return UnifiedCurrencyBar(
          coinBalance: GameStorage.coinBalance,
          gemBalance: GameStorage.gemBalance,
          hintBalance: GameStorage.hintBalance,
          onCoinsTap: () => _tabController.animateTo(1),
          onGemsTap: () => _tabController.animateTo(0),
          onHintsTap: () => _tabController.animateTo(2),
          showAddButton: false,
        );
      },
    );
  }

  Widget _buildPacksList(List<StorePack> packs, {required bool isDiamonds, required EdgeInsets safePadding}) {
    return ListView.builder(
      padding: EdgeInsets.fromLTRB(18, 8, 18, 48 + safePadding.bottom),
      itemCount: packs.length,
      itemBuilder: (context, index) {
        final pack = packs[index];
        return _buildPackCard(pack);
      },
    );
  }

  Widget _buildPackCard(StorePack pack) {
    return Container(
      margin: const EdgeInsets.only(bottom: 14),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(22),
        color: const Color(0xFF131D33).withAlpha(235),
        border: Border.all(
          color: pack.gradientColors.first.withAlpha(140),
          width: 1.5,
        ),
        boxShadow: [
          const BoxShadow(
            color: Color(0x35000000),
            blurRadius: 10,
            offset: Offset(0, 4),
          ),
          BoxShadow(
            color: pack.gradientColors.first.withAlpha(45),
            blurRadius: 14,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Padding(
        padding: const EdgeInsets.all(14),
        child: Row(
          children: [
            // Icon & Bonus Stack
            Stack(
              clipBehavior: Clip.none,
              children: [
                Container(
                  width: 68,
                  height: 68,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    gradient: LinearGradient(
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight,
                      colors: pack.gradientColors,
                    ),
                    boxShadow: [
                      BoxShadow(
                        color: pack.gradientColors.first.withAlpha(120),
                        blurRadius: 12,
                      ),
                    ],
                  ),
                  child: Center(
                    child: Image.asset(
                      pack.imageAsset,
                      width: 40,
                      height: 40,
                    ),
                  ),
                ),
                if (pack.bonus > 0)
                  Positioned(
                    top: -4,
                    right: -4,
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                      decoration: BoxDecoration(
                        color: const Color(0xFFEF4444),
                        borderRadius: BorderRadius.circular(10),
                        border: Border.all(color: Colors.white, width: 1),
                      ),
                      child: Text(
                        '+${pack.bonus}',
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 10,
                          fontWeight: FontWeight.w900,
                        ),
                      ),
                    ),
                  ),
              ],
            ),

            const SizedBox(width: 14),

            // Details
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Flexible(
                        child: Text(
                          pack.title,
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 16,
                            fontWeight: FontWeight.w900,
                          ),
                          overflow: TextOverflow.ellipsis,
                        ),
                      ),
                      if (pack.tag != null) ...[
                        const SizedBox(width: 6),
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 7, vertical: 2),
                          decoration: BoxDecoration(
                            gradient: LinearGradient(colors: pack.gradientColors),
                            borderRadius: BorderRadius.circular(8),
                          ),
                          child: Text(
                            pack.tag!,
                            style: const TextStyle(
                              color: Colors.white,
                              fontSize: 9,
                              fontWeight: FontWeight.w900,
                            ),
                          ),
                        ),
                      ],
                    ],
                  ),
                  const SizedBox(height: 4),
                  Row(
                    children: [
                      Text(
                        '${pack.totalAmount}',
                        style: TextStyle(
                          color: pack.isDiamonds ? const Color(0xFF38BDF8) : const Color(0xFFFFD700),
                          fontSize: 20,
                          fontWeight: FontWeight.w900,
                        ),
                      ),
                      const SizedBox(width: 4),
                      Text(
                        pack.isDiamonds ? tr('gems') : tr('coins'),
                        style: TextStyle(
                          color: Colors.white.withAlpha(200),
                          fontSize: 13,
                          fontWeight: FontWeight.w700,
                        ),
                      ),
                    ],
                  ),
                  Text(
                    'PKR ${pack.pkrPrice}',
                    style: const TextStyle(
                      color: Color(0xFF34D399),
                      fontSize: 11,
                      fontWeight: FontWeight.w700,
                    ),
                  ),
                ],
              ),
            ),

            // Purchase Button
            ElevatedButton(
              onPressed: () => _openCheckoutSheet(pack),
              style: ElevatedButton.styleFrom(
                backgroundColor: pack.gradientColors.first,
                foregroundColor: Colors.white,
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(14),
                  side: const BorderSide(color: Colors.white38, width: 1.2),
                ),
                elevation: 5,
                shadowColor: pack.gradientColors.first.withAlpha(160),
              ),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(
                    '\$${pack.usdPrice.toStringAsFixed(2)}',
                    style: const TextStyle(
                      color: Colors.white,
                      fontSize: 14,
                      fontWeight: FontWeight.w900,
                      shadows: [
                        Shadow(color: Colors.black87, offset: Offset(0, 1), blurRadius: 3),
                      ],
                    ),
                  ),
                  Text(
                    tr('buy'),
                    style: const TextStyle(
                      color: Colors.white,
                      fontSize: 10.5,
                      fontWeight: FontWeight.w900,
                      letterSpacing: 0.6,
                      shadows: [
                        Shadow(color: Colors.black87, offset: Offset(0, 1), blurRadius: 2),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildHintsTab(EdgeInsets safePadding) {
    return SingleChildScrollView(
      padding: EdgeInsets.fromLTRB(18, 6, 18, 48 + safePadding.bottom),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          StoreHintSection(
            title: tr('buy_hints_coins'),
            currencyAsset: 'assets/images/coin.webp',
            prices: const [100, 250, 400, 1000],
            buttonColors: const [Color(0xFF61DA77), Color(0xFF16A947)],
            onBuy: (count, price) => _handleBuyHints(
              count: count,
              price: price,
              useGems: false,
            ),
          ),
          const SizedBox(height: 18),
          StoreHintSection(
            title: tr('buy_hints_gems'),
            currencyAsset: 'assets/images/gem.webp',
            prices: const [10, 25, 45, 120],
            buttonColors: const [Color(0xFF0284C7), Color(0xFF075985)],
            onBuy: (count, price) => _handleBuyHints(
              count: count,
              price: price,
              useGems: true,
            ),
          ),
          const SizedBox(height: 16),
          const StoreHelpPill(),
        ],
      ),
    );
  }

  Widget _buildCircleButton({required IconData icon, required VoidCallback onPressed}) {
    final isRtl = Directionality.of(context) == TextDirection.rtl;
    final displayIcon = (icon == Icons.arrow_back_rounded && isRtl)
        ? Icons.arrow_forward_rounded
        : icon;
    return Material(
      color: Colors.white.withAlpha(25),
      shape: const CircleBorder(),
      child: InkWell(
        customBorder: const CircleBorder(),
        onTap: onPressed,
        child: SizedBox(
          width: 38,
          height: 38,
          child: Icon(displayIcon, color: Colors.white, size: 24),
        ),
      ),
    );
  }
}

// ==========================================
// SECURE CREDIT / DEBIT CARD CHECKOUT MODAL
// ==========================================
class _CheckoutModal extends StatefulWidget {
  final StorePack pack;
  final Future<void> Function(int amount, bool isDiamonds) onSuccess;

  const _CheckoutModal({
    required this.pack,
    required this.onSuccess,
  });

  @override
  State<_CheckoutModal> createState() => _CheckoutModalState();
}

enum _CardBrand { visa, mastercard, paypak, amex, discover, generic }

class _CheckoutModalState extends State<_CheckoutModal> {
  bool _isProcessing = false;
  bool _saveCard = true;
  bool _obscureCvv = true;

  final _cardNumberController = TextEditingController();
  final _cardHolderController = TextEditingController();
  final _cardExpiryController = TextEditingController();
  final _cardCvvController = TextEditingController();

  _CardBrand _cardBrand = _CardBrand.generic;

  @override
  void initState() {
    super.initState();
    _cardNumberController.addListener(_onCardNumberChanged);
    _cardHolderController.addListener(() => setState(() {}));
    _cardExpiryController.addListener(() => setState(() {}));
  }

  void _onCardNumberChanged() {
    final clean = _cardNumberController.text.replaceAll(RegExp(r'\s+'), '');
    _CardBrand detected = _CardBrand.generic;
    if (clean.startsWith('4')) {
      detected = _CardBrand.visa;
    } else if (clean.startsWith(RegExp(r'^(5[1-5]|2[2-7])'))) {
      detected = _CardBrand.mastercard;
    } else if (clean.startsWith(RegExp(r'^(5081|6060|62)'))) {
      detected = _CardBrand.paypak;
    } else if (clean.startsWith(RegExp(r'^(34|37)'))) {
      detected = _CardBrand.amex;
    } else if (clean.startsWith(RegExp(r'^(6011|65|64[4-9])'))) {
      detected = _CardBrand.discover;
    }
    if (detected != _cardBrand) {
      setState(() => _cardBrand = detected);
    } else {
      setState(() {});
    }
  }

  @override
  void dispose() {
    _cardNumberController.dispose();
    _cardHolderController.dispose();
    _cardExpiryController.dispose();
    _cardCvvController.dispose();
    super.dispose();
  }

  bool _isValidLuhn(String cardNumber) {
    if (cardNumber.length < 13 || cardNumber.length > 19) return false;
    int sum = 0;
    bool alternate = false;
    for (int i = cardNumber.length - 1; i >= 0; i--) {
      int digit = int.tryParse(cardNumber[i]) ?? -1;
      if (digit < 0) return false;
      if (alternate) {
        digit *= 2;
        if (digit > 9) digit -= 9;
      }
      sum += digit;
      alternate = !alternate;
    }
    return (sum % 10 == 0);
  }

  Future<void> _processPayment() async {
    final cardNum = _cardNumberController.text.replaceAll(RegExp(r'\s+'), '');
    final holder = _cardHolderController.text.trim();
    final expiry = _cardExpiryController.text.trim();
    final cvv = _cardCvvController.text.trim();

    if (cardNum.length < 15 || cardNum.length > 19) {
      _showError('Please enter a valid 15-16 digit card number');
      return;
    }
    if (!_isValidLuhn(cardNum)) {
      _showError('Invalid card number. Please check the digits.');
      return;
    }
    if (holder.isEmpty || holder.length < 3) {
      _showError('Please enter the full cardholder name');
      return;
    }
    if (expiry.length < 5 || !expiry.contains('/')) {
      _showError('Please enter a valid expiry date (MM/YY)');
      return;
    }
    final expParts = expiry.split('/');
    final month = int.tryParse(expParts[0].trim()) ?? 0;
    if (month < 1 || month > 12) {
      _showError('Invalid expiration month (01-12)');
      return;
    }
    final year = int.tryParse(expParts[1].trim()) ?? 0;
    if (year < 24) {
      _showError('Card has expired. Please use an active card.');
      return;
    }
    if (cvv.length < 3 || cvv.length > 4) {
      _showError('Please enter a valid 3 or 4 digit CVV/CVC');
      return;
    }

    setState(() => _isProcessing = true);
    HapticFeedback.mediumImpact();

    await Future.delayed(const Duration(milliseconds: 1400));
    if (!mounted) return;

    playWinSound();
    triggerSuccessFeedback();
    Navigator.of(context).pop();
    await widget.onSuccess(widget.pack.totalAmount, widget.pack.isDiamonds);
  }

  void _showError(String message) {
    HapticFeedback.lightImpact();
    showGameNotification(
      context: context,
      message: message,
      icon: Icons.error_outline_rounded,
      accentColor: const Color(0xFFEF4444),
      iconColor: const Color(0xFFFCA5A5),
    );
  }

  @override
  Widget build(BuildContext context) {
    final pack = widget.pack;
    final bottomInset = MediaQuery.viewInsetsOf(context).bottom;

    return Directionality(
      textDirection: LanguageController.instance.directionality,
      child: Container(
        constraints: BoxConstraints(
          maxHeight: MediaQuery.of(context).size.height * 0.92,
        ),
        margin: EdgeInsets.only(bottom: bottomInset),
        decoration: const BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.vertical(top: Radius.circular(32)),
          border: Border(
            top: BorderSide(color: Color(0xFFBAE6FD), width: 2),
          ),
          boxShadow: [
            BoxShadow(
              color: Color(0x220F172A),
              blurRadius: 40,
              spreadRadius: 2,
            ),
          ],
        ),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            // Drag handle
            Center(
              child: Container(
                margin: const EdgeInsets.only(top: 10, bottom: 6),
                width: 44,
                height: 4,
                decoration: BoxDecoration(
                  color: const Color(0xFFCBD5E1),
                  borderRadius: BorderRadius.circular(2),
                ),
              ),
            ),

            // Header
            Padding(
              padding: const EdgeInsets.fromLTRB(20, 6, 16, 12),
              child: Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(8),
                    decoration: BoxDecoration(
                      color: const Color(0xFFE0F2FE),
                      shape: BoxShape.circle,
                      border: Border.all(color: const Color(0xFFBAE6FD)),
                    ),
                    child: const Icon(
                      Icons.lock_rounded,
                      color: Color(0xFF0284C7),
                      size: 18,
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          tr('pay_securely'),
                          style: const TextStyle(
                            color: Color(0xFF0F172A),
                            fontSize: 18,
                            fontWeight: FontWeight.w900,
                            letterSpacing: 0.3,
                          ),
                        ),
                        Row(
                          children: [
                            const Icon(Icons.verified_user_rounded, color: Color(0xFF059669), size: 12),
                            const SizedBox(width: 4),
                            const Text(
                              '256-BIT SSL ENCRYPTED • LIVE PAYMENT',
                              style: TextStyle(
                                color: Color(0xFF64748B),
                                fontSize: 10,
                                fontWeight: FontWeight.w800,
                                letterSpacing: 0.6,
                              ),
                            ),
                          ],
                        ),
                      ],
                    ),
                  ),
                  IconButton(
                    icon: const Icon(Icons.close_rounded, color: Color(0xFF64748B)),
                    onPressed: () => Navigator.of(context).pop(),
                  ),
                ],
              ),
            ),

            const Divider(color: Color(0xFFE2E8F0), height: 1),

            // Scrollable Body
            Flexible(
              child: SingleChildScrollView(
                padding: const EdgeInsets.fromLTRB(20, 14, 20, 24),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    // Order Summary Card
                    _buildOrderSummaryCard(pack),
                    const SizedBox(height: 18),

                    // Realistic Virtual Card Preview
                    _buildInteractiveCardPreview(),
                    const SizedBox(height: 20),

                    // Card Input Fields
                    _buildCardForm(),
                    const SizedBox(height: 16),

                    // 1-Click Save Checkbox
                    _buildSaveCardTile(),
                    const SizedBox(height: 16),

                    // Security Guarantee Trust Strip
                    _buildSecurityTrustStrip(),
                    const SizedBox(height: 20),

                    // Pay Now Button
                    _buildPayButton(pack),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildOrderSummaryCard(StorePack pack) {
    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: const Color(0xFFF8FAFC),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: const Color(0xFFE2E8F0)),
      ),
      child: Row(
        children: [
          Container(
            width: 48,
            height: 48,
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(14),
              gradient: LinearGradient(
                colors: pack.gradientColors,
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
              ),
              boxShadow: [
                BoxShadow(
                  color: pack.gradientColors.first.withAlpha(80),
                  blurRadius: 10,
                ),
              ],
            ),
            child: Center(
              child: Image.asset(pack.imageAsset, width: 28, height: 28),
            ),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  pack.title,
                  style: const TextStyle(
                    color: Color(0xFF0F172A),
                    fontSize: 15,
                    fontWeight: FontWeight.w800,
                  ),
                ),
                const SizedBox(height: 2),
                Row(
                  children: [
                    Text(
                      '+${pack.amount} ${pack.isDiamonds ? tr('gems') : tr('coins')}',
                      style: TextStyle(
                        color: pack.isDiamonds ? const Color(0xFF0284C7) : const Color(0xFFD97706),
                        fontSize: 13,
                        fontWeight: FontWeight.w800,
                      ),
                    ),
                    if (pack.bonus > 0) ...[
                      const SizedBox(width: 6),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 1),
                        decoration: BoxDecoration(
                          color: const Color(0xFFEF4444),
                          borderRadius: BorderRadius.circular(6),
                        ),
                        child: Text(
                          '+${pack.bonus} FREE',
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 9,
                            fontWeight: FontWeight.w900,
                          ),
                        ),
                      ),
                    ],
                  ],
                ),
              ],
            ),
          ),
          Column(
            crossAxisAlignment: CrossAxisAlignment.end,
            children: [
              Text(
                '\$${pack.usdPrice.toStringAsFixed(2)}',
                style: const TextStyle(
                  color: Color(0xFF0F172A),
                  fontSize: 18,
                  fontWeight: FontWeight.w900,
                ),
              ),
              const Text(
                'USD',
                style: TextStyle(
                  color: Color(0xFF64748B),
                  fontSize: 10,
                  fontWeight: FontWeight.w800,
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildInteractiveCardPreview() {
    final rawNumber = _cardNumberController.text.replaceAll(RegExp(r'\s+'), '');
    final paddedNumber = rawNumber.padRight(16, '•');
    final formattedNumber =
        '${paddedNumber.substring(0, 4)}  ${paddedNumber.substring(4, 8)}  ${paddedNumber.substring(8, 12)}  ${paddedNumber.substring(12, 16)}';

    final holderText = _cardHolderController.text.trim().isEmpty
        ? 'CARDHOLDER NAME'
        : _cardHolderController.text.trim().toUpperCase();

    final expiryText = _cardExpiryController.text.trim().isEmpty
        ? 'MM/YY'
        : _cardExpiryController.text.trim();

    return Container(
      width: double.infinity,
      height: 195,
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(22),
        gradient: const LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          colors: [
            Color(0xFF1E2640),
            Color(0xFF0F172A),
            Color(0xFF0B0F19),
          ],
        ),
        border: Border.all(color: const Color(0xFF38BDF8).withAlpha(90), width: 1.2),
        boxShadow: [
          BoxShadow(
            color: const Color(0xFF0284C7).withAlpha(50),
            blurRadius: 20,
            offset: const Offset(0, 8),
          ),
          BoxShadow(
            color: Colors.black.withAlpha(160),
            blurRadius: 15,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          // Top Row: Chip & Contactless + Brand
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  // Gold EMV Chip
                  Container(
                    width: 38,
                    height: 28,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(6),
                      gradient: const LinearGradient(
                        colors: [Color(0xFFFFDF7A), Color(0xFFB48325), Color(0xFFE5B446)],
                        begin: Alignment.topLeft,
                        end: Alignment.bottomRight,
                      ),
                      border: Border.all(color: const Color(0xFF6B4706), width: 0.8),
                    ),
                    child: Stack(
                      children: [
                        Center(
                          child: Container(
                            width: 24,
                            height: 16,
                            decoration: BoxDecoration(
                              borderRadius: BorderRadius.circular(3),
                              border: Border.all(color: const Color(0xFF6B4706).withAlpha(120), width: 0.6),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(width: 10),
                  // Contactless icon
                  Transform.rotate(
                    angle: 1.5708,
                    child: const Icon(Icons.wifi_rounded, color: Colors.white70, size: 20),
                  ),
                ],
              ),
              _buildBrandBadge(_cardBrand),
            ],
          ),

          // Middle: Card Number (Monospaced display)
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 4),
            child: Text(
              formattedNumber,
              style: const TextStyle(
                color: Colors.white,
                fontSize: 18,
                fontWeight: FontWeight.w700,
                letterSpacing: 2.2,
                fontFamily: 'monospace',
                shadows: [
                  Shadow(color: Colors.black87, offset: Offset(1, 1), blurRadius: 3),
                ],
              ),
            ),
          ),

          // Bottom Row: Cardholder & Expiry
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'CARDHOLDER',
                      style: TextStyle(
                        color: Colors.white.withAlpha(130),
                        fontSize: 8.5,
                        fontWeight: FontWeight.w900,
                        letterSpacing: 1.2,
                      ),
                    ),
                    const SizedBox(height: 2),
                    Text(
                      holderText,
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 13,
                        fontWeight: FontWeight.w800,
                        letterSpacing: 0.8,
                      ),
                    ),
                  ],
                ),
              ),
              Column(
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  Text(
                    'EXPIRES',
                    style: TextStyle(
                      color: Colors.white.withAlpha(130),
                      fontSize: 8.5,
                      fontWeight: FontWeight.w900,
                      letterSpacing: 1.2,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    expiryText,
                    style: const TextStyle(
                      color: Colors.white,
                      fontSize: 13,
                      fontWeight: FontWeight.w800,
                      letterSpacing: 1.2,
                      fontFamily: 'monospace',
                    ),
                  ),
                ],
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildBrandBadge(_CardBrand brand) {
    switch (brand) {
      case _CardBrand.visa:
        return Container(
          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(6),
          ),
          child: const Text(
            'VISA',
            style: TextStyle(
              color: Color(0xFF1A1F71),
              fontSize: 14,
              fontWeight: FontWeight.w900,
              fontStyle: FontStyle.italic,
              letterSpacing: 1.5,
            ),
          ),
        );
      case _CardBrand.mastercard:
        return SizedBox(
          width: 44,
          height: 26,
          child: Stack(
            children: [
              Positioned(
                left: 2,
                top: 2,
                child: Container(
                  width: 22,
                  height: 22,
                  decoration: const BoxDecoration(
                    color: Color(0xFFEB001B),
                    shape: BoxShape.circle,
                  ),
                ),
              ),
              Positioned(
                right: 2,
                top: 2,
                child: Container(
                  width: 22,
                  height: 22,
                  decoration: BoxDecoration(
                    color: const Color(0xFFF79E1B).withAlpha(220),
                    shape: BoxShape.circle,
                  ),
                ),
              ),
            ],
          ),
        );
      case _CardBrand.paypak:
        return Container(
          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
          decoration: BoxDecoration(
            color: const Color(0xFF006837),
            borderRadius: BorderRadius.circular(6),
          ),
          child: const Text(
            'PayPak',
            style: TextStyle(
              color: Colors.white,
              fontSize: 11,
              fontWeight: FontWeight.w900,
              letterSpacing: 0.5,
            ),
          ),
        );
      case _CardBrand.amex:
        return Container(
          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
          decoration: BoxDecoration(
            color: const Color(0xFF006FCF),
            borderRadius: BorderRadius.circular(6),
          ),
          child: const Text(
            'AMEX',
            style: TextStyle(
              color: Colors.white,
              fontSize: 12,
              fontWeight: FontWeight.w900,
              letterSpacing: 1,
            ),
          ),
        );
      case _CardBrand.discover:
        return Container(
          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
          decoration: BoxDecoration(
            color: const Color(0xFFFF6000),
            borderRadius: BorderRadius.circular(6),
          ),
          child: const Text(
            'DISCOVER',
            style: TextStyle(
              color: Colors.white,
              fontSize: 10,
              fontWeight: FontWeight.w900,
              letterSpacing: 0.8,
            ),
          ),
        );
      case _CardBrand.generic:
        return Container(
          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
          decoration: BoxDecoration(
            color: Colors.white.withAlpha(20),
            borderRadius: BorderRadius.circular(6),
            border: Border.all(color: Colors.white24),
          ),
          child: const Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(Icons.credit_card_rounded, color: Colors.white70, size: 14),
              SizedBox(width: 4),
              Text(
                'CARD',
                style: TextStyle(
                  color: Colors.white70,
                  fontSize: 10,
                  fontWeight: FontWeight.w800,
                  letterSpacing: 1,
                ),
              ),
            ],
          ),
        );
    }
  }

  Widget _buildCardForm() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Card Number
        _buildInputField(
          controller: _cardNumberController,
          label: 'CARD NUMBER',
          hint: '0000 0000 0000 0000',
          prefixIcon: Icons.credit_card_rounded,
          keyboardType: TextInputType.number,
          inputFormatters: [
            FilteringTextInputFormatter.digitsOnly,
            LengthLimitingTextInputFormatter(16),
            _CardNumberFormatter(),
          ],
          suffix: _cardBrand != _CardBrand.generic
              ? Padding(
                  padding: const EdgeInsets.only(right: 12),
                  child: _buildBrandBadge(_cardBrand),
                )
              : null,
        ),
        const SizedBox(height: 14),

        // Cardholder Name
        _buildInputField(
          controller: _cardHolderController,
          label: 'CARDHOLDER NAME',
          hint: 'e.g. ALEX JOHNSON',
          prefixIcon: Icons.person_outline_rounded,
          keyboardType: TextInputType.name,
          textCapitalization: TextCapitalization.characters,
        ),
        const SizedBox(height: 14),

        // Row: Expiry & CVV
        Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Expanded(
              child: _buildInputField(
                controller: _cardExpiryController,
                label: 'EXPIRATION',
                hint: 'MM / YY',
                prefixIcon: Icons.calendar_today_rounded,
                keyboardType: TextInputType.number,
                inputFormatters: [
                  FilteringTextInputFormatter.digitsOnly,
                  LengthLimitingTextInputFormatter(4),
                  _CardExpiryFormatter(),
                ],
              ),
            ),
            const SizedBox(width: 14),
            Expanded(
              child: _buildInputField(
                controller: _cardCvvController,
                label: 'CVV / CVC',
                hint: '123',
                prefixIcon: Icons.security_rounded,
                keyboardType: TextInputType.number,
                obscureText: _obscureCvv,
                inputFormatters: [
                  FilteringTextInputFormatter.digitsOnly,
                  LengthLimitingTextInputFormatter(4),
                ],
                suffix: IconButton(
                  icon: Icon(
                    _obscureCvv ? Icons.visibility_off_outlined : Icons.visibility_outlined,
                    color: const Color(0xFF64748B),
                    size: 18,
                  ),
                  onPressed: () => setState(() => _obscureCvv = !_obscureCvv),
                ),
              ),
            ),
          ],
        ),
      ],
    );
  }

  Widget _buildInputField({
    required TextEditingController controller,
    required String label,
    required String hint,
    required IconData prefixIcon,
    TextInputType keyboardType = TextInputType.text,
    TextCapitalization textCapitalization = TextCapitalization.none,
    bool obscureText = false,
    List<TextInputFormatter>? inputFormatters,
    Widget? suffix,
  }) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          label,
          style: const TextStyle(
            color: Color(0xFF475569),
            fontSize: 11,
            fontWeight: FontWeight.w800,
            letterSpacing: 0.8,
          ),
        ),
        const SizedBox(height: 6),
        Container(
          decoration: BoxDecoration(
            color: const Color(0xFFF8FAFC),
            borderRadius: BorderRadius.circular(16),
            border: Border.all(color: const Color(0xFFE2E8F0), width: 1.2),
          ),
          child: TextField(
            controller: controller,
            keyboardType: keyboardType,
            textCapitalization: textCapitalization,
            obscureText: obscureText,
            inputFormatters: inputFormatters,
            style: const TextStyle(
              color: Color(0xFF0F172A),
              fontSize: 14,
              fontWeight: FontWeight.w700,
            ),
            decoration: InputDecoration(
              isDense: true,
              hintText: hint,
              hintStyle: const TextStyle(
                color: Color(0xFF94A3B8),
                fontSize: 13,
                fontWeight: FontWeight.w500,
              ),
              prefixIcon: Icon(prefixIcon, color: const Color(0xFF0284C7), size: 19),
              suffixIcon: suffix,
              border: InputBorder.none,
              contentPadding: const EdgeInsets.symmetric(horizontal: 14, vertical: 14),
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildSaveCardTile() {
    return InkWell(
      onTap: () => setState(() => _saveCard = !_saveCard),
      borderRadius: BorderRadius.circular(12),
      child: Padding(
        padding: const EdgeInsets.symmetric(vertical: 4),
        child: Row(
          children: [
            SizedBox(
              width: 24,
              height: 24,
              child: Checkbox(
                value: _saveCard,
                onChanged: (val) => setState(() => _saveCard = val ?? true),
                activeColor: const Color(0xFF0284C7),
                checkColor: Colors.white,
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                side: const BorderSide(color: Color(0xFF94A3B8)),
              ),
            ),
            const SizedBox(width: 10),
            const Expanded(
              child: Text(
                'Save card details securely for future 1-tap game purchases',
                style: TextStyle(
                  color: Color(0xFF334155),
                  fontSize: 12,
                  fontWeight: FontWeight.w600,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSecurityTrustStrip() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
      decoration: BoxDecoration(
        color: const Color(0xFFF0FDF4),
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: const Color(0xFFBBF7D0)),
      ),
      child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              _buildTrustBadge(Icons.shield_rounded, 'PCI-DSS LEVEL 1'),
              Container(width: 1, height: 16, color: const Color(0xFFDCFCE7)),
              _buildTrustBadge(Icons.lock_rounded, '256-BIT SSL'),
              Container(width: 1, height: 16, color: const Color(0xFFDCFCE7)),
              _buildTrustBadge(Icons.bolt_rounded, 'INSTANT CREDIT'),
            ],
          ),
          const SizedBox(height: 8),
          const Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(Icons.account_balance_rounded, color: Color(0xFF10B981), size: 13),
              SizedBox(width: 6),
              Text(
                'Settlement Destination: Meezan Bank Merchant Account',
                style: TextStyle(
                  color: Color(0xFF15803D),
                  fontSize: 10,
                  fontWeight: FontWeight.w700,
                  letterSpacing: 0.3,
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildTrustBadge(IconData icon, String text) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        Icon(icon, color: const Color(0xFF16A34A), size: 13),
        const SizedBox(width: 5),
        Text(
          text,
          style: const TextStyle(
            color: Color(0xFF166534),
            fontSize: 9.5,
            fontWeight: FontWeight.w800,
            letterSpacing: 0.4,
          ),
        ),
      ],
    );
  }

  Widget _buildPayButton(StorePack pack) {
    return Container(
      width: double.infinity,
      height: 54,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(18),
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
        onPressed: _isProcessing ? null : _processPayment,
        style: ElevatedButton.styleFrom(
          backgroundColor: Colors.transparent,
          shadowColor: Colors.transparent,
          foregroundColor: Colors.white,
          disabledBackgroundColor: Colors.transparent,
          minimumSize: const Size(double.infinity, 54),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18)),
        ),
      child: _isProcessing
          ? const Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                SizedBox(
                  width: 20,
                  height: 20,
                  child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2.4),
                ),
                SizedBox(width: 12),
                Text(
                  'Authorizing Card Payment...',
                  style: TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.w800,
                    letterSpacing: 0.5,
                  ),
                ),
              ],
            )
          : Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Icon(Icons.lock_rounded, size: 18),
                const SizedBox(width: 8),
                Text(
                  'Pay with Card • \$${pack.usdPrice.toStringAsFixed(2)} USD (Rs. ${pack.pkrPrice})',
                  style: const TextStyle(
                    fontSize: 14.5,
                    fontWeight: FontWeight.w900,
                    letterSpacing: 0.4,
                  ),
                ),
              ],
            ),
      ),
    );
  }
}

// ==========================================
// CARD INPUT FORMATTERS
// ==========================================
class _CardNumberFormatter extends TextInputFormatter {
  @override
  TextEditingValue formatEditUpdate(
    TextEditingValue oldValue,
    TextEditingValue newValue,
  ) {
    final text = newValue.text.replaceAll(' ', '');
    final buffer = StringBuffer();
    for (int i = 0; i < text.length; i++) {
      if (i > 0 && i % 4 == 0) {
        buffer.write(' ');
      }
      buffer.write(text[i]);
    }
    final formatted = buffer.toString();
    return TextEditingValue(
      text: formatted,
      selection: TextSelection.collapsed(offset: formatted.length),
    );
  }
}

class _CardExpiryFormatter extends TextInputFormatter {
  @override
  TextEditingValue formatEditUpdate(
    TextEditingValue oldValue,
    TextEditingValue newValue,
  ) {
    final text = newValue.text.replaceAll('/', '').replaceAll(' ', '');
    final buffer = StringBuffer();
    for (int i = 0; i < text.length; i++) {
      if (i == 2) {
        buffer.write(' / ');
      }
      buffer.write(text[i]);
    }
    final formatted = buffer.toString();
    return TextEditingValue(
      text: formatted,
      selection: TextSelection.collapsed(offset: formatted.length),
    );
  }
}
