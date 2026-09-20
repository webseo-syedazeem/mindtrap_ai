import 'package:flutter_test/flutter_test.dart';

import 'package:mindtrap_ai/main.dart';

void main() {
  testWidgets('MindTrap AI home screen shows menu options', (
    WidgetTester tester,
  ) async {
    await tester.pumpWidget(const MindTrapApp());

    expect(find.text('MindTrap AI'), findsOneWidget);
    expect(find.text('Play Game'), findsOneWidget);
    expect(find.text('Daily Puzzle'), findsOneWidget);
    expect(find.text('Stats'), findsOneWidget);
    expect(find.text('Settings'), findsOneWidget);
  });
}
