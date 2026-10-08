# -*- coding: utf-8 -*-
with open('lib/screens/map_your_mind_screen.dart', 'r', encoding='utf-8') as f:
    text = f.read()

target = """      child: Stack(
        children: [
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                width: 36,
                height: 36,
                decoration: BoxDecoration(
                  color: iconColor.withValues(alpha: 0.12),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Icon(icon, color: iconColor, size: 20),
              ),
              const SizedBox(height: 8),
              Text(
                title,
                style: const TextStyle(
                  color: Color(0xFF0F172A),
                  fontWeight: FontWeight.w800,
                  fontSize: 13,
                ),
              ),
              const SizedBox(height: 2),
              Text(
                subtitle,
                style: TextStyle(
                  color: isSelected ? const Color(0xFF2563EB) : const Color(0xFF64748B),
                  fontSize: 11,
                  fontWeight: isSelected ? FontWeight.w600 : FontWeight.w500,
                ),
              ),
            ],
          ),
          if (isSelected)
            Positioned(
              top: 0,
              right: 0,
              child: Container(
                width: 20,
                height: 20,
                decoration: const BoxDecoration(
                  shape: BoxShape.circle,
                  color: Color(0xFF2563EB),
                ),
                child: const Icon(Icons.check_rounded, size: 14, color: Colors.white),
              ),
            ),
        ],
      ),"""

repl = """      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Container(
                width: 36,
                height: 36,
                decoration: BoxDecoration(
                  color: iconColor.withValues(alpha: 0.12),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Icon(icon, color: iconColor, size: 20),
              ),
              if (isSelected)
                Container(
                  width: 22,
                  height: 22,
                  decoration: const BoxDecoration(
                    shape: BoxShape.circle,
                    color: Color(0xFF2563EB),
                  ),
                  child: const Icon(Icons.check_rounded, size: 14, color: Colors.white),
                )
              else
                const SizedBox(width: 22, height: 22),
            ],
          ),
          const SizedBox(height: 8),
          Text(
            title,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
            style: const TextStyle(
              color: Color(0xFF0F172A),
              fontWeight: FontWeight.w800,
              fontSize: 13,
            ),
          ),
          const SizedBox(height: 2),
          Text(
            subtitle,
            maxLines: 2,
            overflow: TextOverflow.ellipsis,
            style: TextStyle(
              color: isSelected ? const Color(0xFF2563EB) : const Color(0xFF64748B),
              fontSize: 11,
              fontWeight: isSelected ? FontWeight.w600 : FontWeight.w500,
            ),
          ),
        ],
      ),"""

if target in text:
    text = text.replace(target, repl)
    with open('lib/screens/map_your_mind_screen.dart', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Patched map_your_mind_screen.dart successfully!")
else:
    print("Target block not found in map_your_mind_screen.dart!")
