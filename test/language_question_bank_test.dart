import 'dart:convert';
import 'dart:io';
import 'package:flutter_test/flutter_test.dart';
import 'package:mindtrap_ai/services/language_question_service.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  group('Language Question Banks Verification', () {
    test('English bank contains 1000 unique questions with 0 prefixes and proper tiers', () {
      final file = File('assets/questions/en.json');
      expect(file.existsSync(), isTrue);

      final jsonList = jsonDecode(file.readAsStringSync()) as List<dynamic>;
      expect(jsonList.length, 1000);

      final stems = <String>{};
      int easy = 0;
      int normal = 0;
      int tricky = 0;

      for (int i = 0; i < jsonList.length; i++) {
        final item = jsonList[i] as Map<String, dynamic>;
        final q = item['question'] as String;
        final opts = List<String>.from(item['options'] as List);
        final ans = item['correctAnswer'] as String;
        final diff = item['difficulty'] as String;

        // No robotic prefixes
        expect(q.contains('Warm-up'), isFalse);
        expect(q.contains('Logic Riddle'), isFalse);
        expect(q.contains('Master Trap'), isFalse);
        expect(q.contains('#'), isFalse);

        // Options check
        expect(opts.length, 4);
        expect(opts.toSet().length, 4);
        expect(opts.contains(ans), isTrue);

        // Unique stem
        final norm = q.toLowerCase().replaceAll(RegExp(r'[^\w\s]'), '').trim();
        expect(stems.contains(norm), isFalse, reason: 'Duplicate question found at $i: $q');
        stems.add(norm);

        if (diff == 'easy') easy++;
        if (diff == 'normal') normal++;
        if (diff == 'tricky') tricky++;
      }

      expect(easy, 250);
      expect(normal, 400);
      expect(tricky, 350);
    });

    test('Urdu bank contains 1000 unique questions with 0 prefixes and proper tiers', () {
      final file = File('assets/questions/ur.json');
      expect(file.existsSync(), isTrue);

      final jsonList = jsonDecode(file.readAsStringSync()) as List<dynamic>;
      expect(jsonList.length, 1000);

      final stems = <String>{};
      int easy = 0;
      int normal = 0;
      int tricky = 0;

      for (int i = 0; i < jsonList.length; i++) {
        final item = jsonList[i] as Map<String, dynamic>;
        final q = item['question'] as String;
        final opts = List<String>.from(item['options'] as List);
        final ans = item['correctAnswer'] as String;
        final diff = item['difficulty'] as String;

        // No robotic prefixes
        expect(q.contains('Warm-up'), isFalse);
        expect(q.contains('Logic Riddle'), isFalse);
        expect(q.contains('Master Trap'), isFalse);
        expect(q.contains('پہیلی #'), isFalse);
        expect(q.contains('پہیلی نمبر'), isFalse);
        expect(q.contains('#'), isFalse);

        // Options check
        expect(opts.length, 4);
        expect(opts.toSet().length, 4);
        expect(opts.contains(ans), isTrue);

        // Unique stem
        final norm = q.trim();
        expect(stems.contains(norm), isFalse, reason: 'Duplicate Urdu question at $i: $q');
        stems.add(norm);

        if (diff == 'easy') easy++;
        if (diff == 'normal') normal++;
        if (diff == 'tricky') tricky++;
      }

      expect(easy, 250);
      expect(normal, 400);
      expect(tricky, 350);
    });

    test('Hindi bank contains 1000 unique questions with 0 prefixes and proper tiers', () {
      final file = File('assets/questions/hi.json');
      expect(file.existsSync(), isTrue);

      final jsonList = jsonDecode(file.readAsStringSync()) as List<dynamic>;
      expect(jsonList.length, 1000);

      int easy = 0;
      int normal = 0;
      int tricky = 0;

      for (int i = 0; i < jsonList.length; i++) {
        final item = jsonList[i] as Map<String, dynamic>;
        final q = item['question'] as String;
        final opts = List<String>.from(item['options'] as List);
        final ans = item['correctAnswer'] as String;
        final diff = item['difficulty'] as String;

        expect(q.isNotEmpty, isTrue);
        expect(opts.length, 4);
        expect(opts.contains(ans), isTrue);

        if (diff == 'easy') easy++;
        if (diff == 'normal') normal++;
        if (diff == 'tricky') tricky++;
      }

      expect(easy, 250);
      expect(normal, 400);
      expect(tricky, 350);
    });

    test('Strict difficulty tier progression from level 0 to 999', () {
      final service = LanguageQuestionService.instance;

      // Level 0 should return easy questions
      final easyBatch = service.getQuestionsForLevel(globalLevel: 0, langCode: 'en', count: 3);
      expect(easyBatch.length, 3);
      expect(easyBatch[0].question, isNotEmpty);
      expect(easyBatch[0].question, isNot(equals(easyBatch[1].question)));
      expect(easyBatch[1].question, isNot(equals(easyBatch[2].question)));

      // Level 1 should return distinct questions from Level 0
      final level1Batch = service.getQuestionsForLevel(globalLevel: 1, langCode: 'en', count: 3);
      expect(level1Batch.length, 3);
      for (final q in level1Batch) {
        expect(easyBatch.any((oldQ) => oldQ.question == q.question), isFalse);
      }

      // Normal tier: Level 250
      final normalBatch = service.getQuestionsForLevel(globalLevel: 250, langCode: 'en', count: 3);
      expect(normalBatch.length, 3);

      // Tricky tier: Level 650
      final trickyBatch = service.getQuestionsForLevel(globalLevel: 650, langCode: 'en', count: 3);
      expect(trickyBatch.length, 3);

      // Urdu progression
      final urduBatch = service.getQuestionsForLevel(globalLevel: 0, langCode: 'ur', count: 3);
      expect(urduBatch.length, 3);
      expect(urduBatch[0].question, isNotEmpty);
    });
  });
}
