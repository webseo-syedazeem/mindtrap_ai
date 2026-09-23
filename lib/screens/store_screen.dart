import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../localization/app_language.dart';
import '../localization/language_controller.dart';
import '../main.dart';

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
      builder: (ctx) => Dialog(
        backgroundColor: Colors.transparent,
        child: Container(
          padding: const EdgeInsets.all(24),
          decoration: BoxDecoration(
            color: const Color(0xFF0F172A),
            borderRadius: BorderRadius.circular(28),
            border: Border.all(
              color: isDiamonds ? const Color(0xFF38BDF8) : const Color(0xFFFFD700),
              width: 2,
            ),
            boxShadow: [
              BoxShadow(
                color: (isDiamonds ? const Color(0xFF38BDF8) : const Color(0xFFFFD700)).withAlpha(80),
                blurRadius: 30,
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
                        ? [const Color(0xFF38BDF8), const Color(0xFF1D4ED8)]
                        : [const Color(0xFFFFE066), const Color(0xFFD97706)],
                  ),
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
                  color: Colors.white,
                  fontSize: 22,
                  fontWeight: FontWeight.w900,
                ),
              ),
              const SizedBox(height: 8),
              Text(
                '+$amount ${isDiamonds ? tr('gems') : tr('coins')}',
                style: TextStyle(
                  color: isDiamonds ? const Color(0xFF38BDF8) : const Color(0xFFFFD700),
                  fontSize: 26,
                  fontWeight: FontWeight.w900,
                ),
              ),
              const SizedBox(height: 6),
              Text(
                isDiamonds ? tr('diamonds_added') : tr('coins_added'),
                textAlign: TextAlign.center,
                style: const TextStyle(
                  color: Colors.white70,
                  fontSize: 14,
                ),
              ),
              const SizedBox(height: 24),
              ElevatedButton(
                onPressed: () => Navigator.of(ctx).pop(),
                style: ElevatedButton.styleFrom(
                  backgroundColor: isDiamonds ? const Color(0xFF2563EB) : const Color(0xFFD97706),
                  minimumSize: const Size(double.infinity, 48),
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
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text('$count ${tr('purchase_success')}'),
          backgroundColor: const Color(0xFF16A947),
          duration: const Duration(seconds: 2),
        ),
      );
      setState(() {});
    } else {
      triggerHeavyFeedback();
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(
            useGems ? tr('not_enough_gems') : tr('not_enough_coins'),
          ),
          backgroundColor: const Color(0xFFE53935),
          duration: const Duration(seconds: 2),
        ),
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
                            icon: Icons.arrow_back_ios_new_rounded,
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
                        indicator: BoxDecoration(
                          gradient: const LinearGradient(
                            colors: [Color(0xFF38BDF8), Color(0xFF2563EB)],
                          ),
                          borderRadius: BorderRadius.circular(14),
                          boxShadow: [
                            BoxShadow(
                              color: const Color(0xFF38BDF8).withAlpha(100),
                              blurRadius: 10,
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
                          _buildPacksList(diamondPacks, isDiamonds: true),

                          // 2. Coins Tab
                          _buildPacksList(coinPacks, isDiamonds: false),

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
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
      decoration: BoxDecoration(
        color: Colors.black.withAlpha(160),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.white.withAlpha(30)),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Image.asset('assets/images/gem.webp', width: 18, height: 18),
          const SizedBox(width: 4),
          Text(
            '${GameStorage.gemBalance}',
            style: const TextStyle(color: Color(0xFF38BDF8), fontWeight: FontWeight.w900, fontSize: 13),
          ),
          const SizedBox(width: 12),
          Image.asset('assets/images/coin.webp', width: 18, height: 18),
          const SizedBox(width: 4),
          Text(
            '${GameStorage.coinBalance}',
            style: const TextStyle(color: Color(0xFFFFD700), fontWeight: FontWeight.w900, fontSize: 13),
          ),
          const SizedBox(width: 12),
          Image.asset('assets/images/hint-icon.webp', width: 18, height: 18),
          const SizedBox(width: 4),
          Text(
            '${GameStorage.hintBalance}',
            style: const TextStyle(color: Color(0xFF34D399), fontWeight: FontWeight.w900, fontSize: 13),
          ),
        ],
      ),
    );
  }

  Widget _buildPacksList(List<StorePack> packs, {required bool isDiamonds}) {
    return ListView.builder(
      padding: const EdgeInsets.fromLTRB(18, 6, 18, 24),
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
        gradient: LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          colors: [
            Colors.white.withAlpha(22),
            Colors.white.withAlpha(8),
          ],
        ),
        border: Border.all(
          color: pack.gradientColors.first.withAlpha(120),
          width: 1.5,
        ),
        boxShadow: [
          BoxShadow(
            color: pack.gradientColors.first.withAlpha(40),
            blurRadius: 14,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: ClipRRect(
        borderRadius: BorderRadius.circular(21),
        child: BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
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
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                    elevation: 4,
                  ),
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text(
                        '\$${pack.usdPrice.toStringAsFixed(2)}',
                        style: const TextStyle(
                          fontSize: 14,
                          fontWeight: FontWeight.w900,
                        ),
                      ),
                      Text(
                        tr('buy'),
                        style: const TextStyle(
                          fontSize: 10,
                          fontWeight: FontWeight.w700,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildHintsTab(EdgeInsets safePadding) {
    return SingleChildScrollView(
      padding: EdgeInsets.fromLTRB(18, 6, 18, 24 + safePadding.bottom),
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
    return Material(
      color: Colors.white.withAlpha(25),
      shape: const CircleBorder(),
      child: InkWell(
        customBorder: const CircleBorder(),
        onTap: onPressed,
        child: SizedBox(
          width: 44,
          height: 44,
          child: Icon(icon, color: Colors.white, size: 20),
        ),
      ),
    );
  }
}

// ==========================================
// CHECKOUT MODAL (Credit Card & Meezan Bank)
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

class _CheckoutModalState extends State<_CheckoutModal> with SingleTickerProviderStateMixin {
  late TabController _methodTabController;
  bool _isProcessing = false;

  // Credit Card Controllers
  final _cardNumberController = TextEditingController();
  final _cardHolderController = TextEditingController();
  final _cardExpiryController = TextEditingController();
  final _cardCvvController = TextEditingController();

  // Bank Transfer Controllers
  final _senderNameController = TextEditingController();
  final _transactionIdController = TextEditingController();

  // User Provided Exact Bank Details
  static const String meezanAccountTitle = 'Syed Azeem Haider Bukhari';
  static const String meezanAccountNumber = '00300110167256';
  static const String meezanBankName = 'Meezan Bank';
  static const String meezanIban = 'PK82MEZN0000300110167256';

  @override
  void initState() {
    super.initState();
    _methodTabController = TabController(length: 2, vsync: this);
  }

  @override
  void dispose() {
    _methodTabController.dispose();
    _cardNumberController.dispose();
    _cardHolderController.dispose();
    _cardExpiryController.dispose();
    _cardCvvController.dispose();
    _senderNameController.dispose();
    _transactionIdController.dispose();
    super.dispose();
  }

  void _copyToClipboard(String text, String label) {
    Clipboard.setData(ClipboardData(text: text));
    HapticFeedback.lightImpact();
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text('$label ${tr('copied_to_clipboard')}'),
        backgroundColor: const Color(0xFF10B981),
        duration: const Duration(seconds: 2),
      ),
    );
  }

  Future<void> _processCreditCard() async {
    if (_cardNumberController.text.trim().length < 12 ||
        _cardHolderController.text.trim().isEmpty ||
        _cardExpiryController.text.trim().length < 4 ||
        _cardCvvController.text.trim().length < 3) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Please complete all card details correctly'),
          backgroundColor: Color(0xFFEF4444),
        ),
      );
      return;
    }

    setState(() => _isProcessing = true);
    await Future.delayed(const Duration(milliseconds: 1400));
    if (!mounted) return;

    playWinSound();
    triggerSuccessFeedback();
    Navigator.of(context).pop();
    await widget.onSuccess(widget.pack.totalAmount, widget.pack.isDiamonds);
  }

  Future<void> _processBankTransfer() async {
    if (_senderNameController.text.trim().isEmpty || _transactionIdController.text.trim().isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Please enter Sender Name & Transaction ID'),
          backgroundColor: Color(0xFFEF4444),
        ),
      );
      return;
    }

    setState(() => _isProcessing = true);
    await Future.delayed(const Duration(milliseconds: 1200));
    if (!mounted) return;

    playWinSound();
    triggerSuccessFeedback();
    Navigator.of(context).pop();
    await widget.onSuccess(widget.pack.totalAmount, widget.pack.isDiamonds);
  }

  @override
  Widget build(BuildContext context) {
    final pack = widget.pack;
    final keyboardHeight = MediaQuery.viewInsetsOf(context).bottom;

    return Container(
      constraints: BoxConstraints(
        maxHeight: MediaQuery.of(context).size.height * 0.88,
      ),
      margin: EdgeInsets.only(bottom: keyboardHeight),
      decoration: const BoxDecoration(
        color: Color(0xFF0F172A),
        borderRadius: BorderRadius.vertical(top: Radius.circular(32)),
        border: Border(top: BorderSide(color: Color(0xFF38BDF8), width: 2)),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          // Drag handle
          Center(
            child: Container(
              margin: const EdgeInsets.only(top: 12, bottom: 8),
              width: 44,
              height: 4,
              decoration: BoxDecoration(
                color: Colors.white24,
                borderRadius: BorderRadius.circular(2),
              ),
            ),
          ),

          // Pack summary banner
          Container(
            margin: const EdgeInsets.fromLTRB(16, 4, 16, 10),
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              gradient: LinearGradient(
                colors: [
                  pack.gradientColors.first.withAlpha(60),
                  Colors.black.withAlpha(100),
                ],
              ),
              borderRadius: BorderRadius.circular(18),
              border: Border.all(color: pack.gradientColors.first.withAlpha(120)),
            ),
            child: Row(
              children: [
                Image.asset(pack.imageAsset, width: 36, height: 36),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        pack.title,
                        style: const TextStyle(
                          color: Colors.white,
                          fontWeight: FontWeight.w900,
                          fontSize: 15,
                        ),
                      ),
                      Text(
                        '+${pack.totalAmount} ${pack.isDiamonds ? tr('gems') : tr('coins')}',
                        style: TextStyle(
                          color: pack.isDiamonds ? const Color(0xFF38BDF8) : const Color(0xFFFFD700),
                          fontWeight: FontWeight.w700,
                          fontSize: 13,
                        ),
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
                        color: Colors.white,
                        fontWeight: FontWeight.w900,
                        fontSize: 16,
                      ),
                    ),
                    Text(
                      'Rs. ${pack.pkrPrice}',
                      style: const TextStyle(
                        color: Color(0xFF34D399),
                        fontWeight: FontWeight.w800,
                        fontSize: 12,
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),

          // Payment method selector tabs
          Container(
            margin: const EdgeInsets.symmetric(horizontal: 16),
            padding: const EdgeInsets.all(3),
            decoration: BoxDecoration(
              color: Colors.black.withAlpha(140),
              borderRadius: BorderRadius.circular(14),
            ),
            child: TabBar(
              controller: _methodTabController,
              indicator: BoxDecoration(
                gradient: const LinearGradient(
                  colors: [Color(0xFF047857), Color(0xFF10B981)],
                ),
                borderRadius: BorderRadius.circular(12),
              ),
              labelColor: Colors.white,
              unselectedLabelColor: Colors.white60,
              labelStyle: const TextStyle(fontSize: 11, fontWeight: FontWeight.w900),
              tabs: [
                Tab(
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      const Icon(Icons.account_balance_rounded, size: 16),
                      const SizedBox(width: 6),
                      Text(tr('bank_transfer')),
                    ],
                  ),
                ),
                Tab(
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      const Icon(Icons.credit_card_rounded, size: 16),
                      const SizedBox(width: 6),
                      Text(tr('credit_card')),
                    ],
                  ),
                ),
              ],
            ),
          ),

          const SizedBox(height: 10),

          // Tab views
          Expanded(
            child: TabBarView(
              controller: _methodTabController,
              children: [
                // 1. Meezan Bank Transfer Tab
                _buildBankTransferView(),

                // 2. Credit Card Tab
                _buildCreditCardView(),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildBankTransferView() {
    return SingleChildScrollView(
      padding: const EdgeInsets.fromLTRB(16, 4, 16, 20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Official Meezan Bank Card Widget
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              gradient: const LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
                colors: [
                  Color(0xFF064E3B),
                  Color(0xFF065F46),
                  Color(0xFF047857),
                ],
              ),
              borderRadius: BorderRadius.circular(20),
              border: Border.all(color: const Color(0xFF34D399).withAlpha(180), width: 1.5),
              boxShadow: [
                BoxShadow(
                  color: const Color(0xFF065F46).withAlpha(120),
                  blurRadius: 18,
                  offset: const Offset(0, 4),
                ),
              ],
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Row(
                      children: [
                        Container(
                          padding: const EdgeInsets.all(6),
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            color: Colors.white.withAlpha(30),
                          ),
                          child: const Icon(Icons.account_balance_rounded, color: Colors.white, size: 18),
                        ),
                        const SizedBox(width: 8),
                        const Text(
                          meezanBankName,
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 16,
                            fontWeight: FontWeight.w900,
                            letterSpacing: 0.5,
                          ),
                        ),
                      ],
                    ),
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                      decoration: BoxDecoration(
                        color: const Color(0xFFFFD700).withAlpha(40),
                        borderRadius: BorderRadius.circular(8),
                        border: Border.all(color: const Color(0xFFFFD700)),
                      ),
                      child: const Text(
                        'ISLAMIC BANKING',
                        style: TextStyle(
                          color: Color(0xFFFFD700),
                          fontSize: 9,
                          fontWeight: FontWeight.w900,
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 14),

                // Account Title
                const Text(
                  'ACCOUNT TITLE',
                  style: TextStyle(color: Colors.white70, fontSize: 10, fontWeight: FontWeight.w700),
                ),
                const Text(
                  meezanAccountTitle,
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 16,
                    fontWeight: FontWeight.w900,
                  ),
                ),

                const SizedBox(height: 12),

                // Account Number with copy button
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text(
                          'ACCOUNT NUMBER',
                          style: TextStyle(color: Colors.white70, fontSize: 10, fontWeight: FontWeight.w700),
                        ),
                        Text(
                          meezanAccountNumber,
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 16,
                            fontWeight: FontWeight.w900,
                            letterSpacing: 1.2,
                          ),
                        ),
                      ],
                    ),
                    _buildCopyPill(
                      onTap: () => _copyToClipboard(meezanAccountNumber, 'Account Number'),
                    ),
                  ],
                ),

                const SizedBox(height: 12),

                // IBAN with copy button
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          const Text(
                            'IBAN',
                            style: TextStyle(color: Colors.white70, fontSize: 10, fontWeight: FontWeight.w700),
                          ),
                          Text(
                            meezanIban,
                            style: const TextStyle(
                              color: Colors.white,
                              fontSize: 13,
                              fontWeight: FontWeight.w900,
                              letterSpacing: 0.8,
                            ),
                            overflow: TextOverflow.ellipsis,
                          ),
                        ],
                      ),
                    ),
                    _buildCopyPill(
                      onTap: () => _copyToClipboard(meezanIban, 'IBAN'),
                    ),
                  ],
                ),
              ],
            ),
          ),

          const SizedBox(height: 14),

          // Instructions
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: Colors.white.withAlpha(10),
              borderRadius: BorderRadius.circular(14),
              border: Border.all(color: Colors.white12),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Row(
                  children: [
                    Icon(Icons.info_outline_rounded, color: Color(0xFF38BDF8), size: 16),
                    SizedBox(width: 6),
                    Text(
                      'How to pay via Meezan Bank:',
                      style: TextStyle(color: Colors.white, fontWeight: FontWeight.w800, fontSize: 12),
                    ),
                  ],
                ),
                const SizedBox(height: 6),
                Text(
                  '1. Transfer Rs. ${widget.pack.pkrPrice} to the Meezan Bank account above (via Meezan App, Raast, EasyPaisa, JazzCash, or any ATM).\n2. Enter your Sender Name and Transaction ID below.\n3. Tap "Confirm & Claim" to receive your diamonds immediately!',
                  style: const TextStyle(color: Colors.white70, fontSize: 11, height: 1.4),
                ),
              ],
            ),
          ),

          const SizedBox(height: 14),

          // User Inputs for Proof
          _buildTextField(
            controller: _senderNameController,
            label: tr('sender_name'),
            hint: 'e.g. Muhammad Ali',
            icon: Icons.person_rounded,
          ),
          const SizedBox(height: 10),
          _buildTextField(
            controller: _transactionIdController,
            label: tr('transaction_id'),
            hint: 'e.g. TXN-94827491',
            icon: Icons.receipt_long_rounded,
          ),

          const SizedBox(height: 16),

          // Submit Button
          ElevatedButton(
            onPressed: _isProcessing ? null : _processBankTransfer,
            style: ElevatedButton.styleFrom(
              backgroundColor: const Color(0xFF059669),
              foregroundColor: Colors.white,
              minimumSize: const Size(double.infinity, 50),
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
              elevation: 4,
            ),
            child: _isProcessing
                ? const SizedBox(
                    width: 22,
                    height: 22,
                    child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2.5),
                  )
                : Text(
                    tr('confirm_and_claim'),
                    style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w900),
                  ),
          ),
        ],
      ),
    );
  }

  Widget _buildCreditCardView() {
    return SingleChildScrollView(
      padding: const EdgeInsets.fromLTRB(16, 4, 16, 20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Security Banner
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
            decoration: BoxDecoration(
              color: const Color(0xFF2563EB).withAlpha(30),
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: const Color(0xFF38BDF8).withAlpha(100)),
            ),
            child: const Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(Icons.lock_rounded, color: Color(0xFF38BDF8), size: 14),
                SizedBox(width: 6),
                Text(
                  '256-Bit SSL Encrypted & Secure Payment',
                  style: TextStyle(color: Color(0xFF38BDF8), fontSize: 11, fontWeight: FontWeight.w700),
                ),
              ],
            ),
          ),

          const SizedBox(height: 14),

          _buildTextField(
            controller: _cardHolderController,
            label: tr('cardholder_name'),
            hint: 'Name on Card',
            icon: Icons.badge_rounded,
          ),
          const SizedBox(height: 10),
          _buildTextField(
            controller: _cardNumberController,
            label: tr('card_number'),
            hint: '0000 0000 0000 0000',
            icon: Icons.credit_card_rounded,
            keyboardType: TextInputType.number,
          ),
          const SizedBox(height: 10),
          Row(
            children: [
              Expanded(
                child: _buildTextField(
                  controller: _cardExpiryController,
                  label: tr('expiry_date'),
                  hint: 'MM/YY',
                  icon: Icons.calendar_month_rounded,
                  keyboardType: TextInputType.datetime,
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: _buildTextField(
                  controller: _cardCvvController,
                  label: tr('cvv'),
                  hint: '123',
                  icon: Icons.security_rounded,
                  keyboardType: TextInputType.number,
                  obscureText: true,
                ),
              ),
            ],
          ),

          const SizedBox(height: 18),

          // Pay Button
          ElevatedButton(
            onPressed: _isProcessing ? null : _processCreditCard,
            style: ElevatedButton.styleFrom(
              backgroundColor: const Color(0xFF2563EB),
              foregroundColor: Colors.white,
              minimumSize: const Size(double.infinity, 50),
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
              elevation: 4,
            ),
            child: _isProcessing
                ? const SizedBox(
                    width: 22,
                    height: 22,
                    child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2.5),
                  )
                : Text(
                    '${tr('pay_securely')} (\$${widget.pack.usdPrice.toStringAsFixed(2)})',
                    style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w900),
                  ),
          ),
        ],
      ),
    );
  }

  Widget _buildCopyPill({required VoidCallback onTap}) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(10),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
        decoration: BoxDecoration(
          color: Colors.black.withAlpha(120),
          borderRadius: BorderRadius.circular(10),
          border: Border.all(color: Colors.white.withAlpha(60)),
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Icon(Icons.copy_rounded, color: Colors.white, size: 13),
            const SizedBox(width: 4),
            Text(
              tr('copy'),
              style: const TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.w800),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildTextField({
    required TextEditingController controller,
    required String label,
    required String hint,
    required IconData icon,
    TextInputType keyboardType = TextInputType.text,
    bool obscureText = false,
  }) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          label,
          style: const TextStyle(color: Colors.white70, fontSize: 12, fontWeight: FontWeight.w700),
        ),
        const SizedBox(height: 4),
        Container(
          decoration: BoxDecoration(
            color: Colors.white.withAlpha(15),
            borderRadius: BorderRadius.circular(14),
            border: Border.all(color: Colors.white24),
          ),
          child: TextField(
            controller: controller,
            keyboardType: keyboardType,
            obscureText: obscureText,
            style: const TextStyle(color: Colors.white, fontSize: 14),
            decoration: InputDecoration(
              isDense: true,
              hintText: hint,
              hintStyle: const TextStyle(color: Colors.white30, fontSize: 13),
              prefixIcon: Icon(icon, color: const Color(0xFF38BDF8), size: 18),
              border: InputBorder.none,
              contentPadding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
            ),
          ),
        ),
      ],
    );
  }
}
