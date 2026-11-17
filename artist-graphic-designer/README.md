# Artist & Graphic Designer Skill

**مهارة عربية عامة تربط التفكير الفني والتصميم الجرافيكي باستراتيجية التسويق وإنتاج الصور بالذكاء الاصطناعي والتحرير الاحترافي عبر Adobe.**

الهدف ليس جعل النموذج ينتج صورًا أكثر زخرفة؛ بل تحسين فهمه للمهمة والبيزنس والجمهور والـInsight، ثم العصف الذهني وتطوير المفاهيم والتوجيه الفني والتكوين والتنفيذ والنقد والتسليم والتعلم من الأداء.

## ما الجديد في 0.4.0؟

- إضافة Marketing-led Design Workflow من فهم المهمة حتى قياس الأداء.
- ربط Business Goal وMarketing Objective وCommunication Objective.
- إضافة Consumer Insight وCreative Brief وCTA وKPI.
- إضافة مسار واضح لاختيار AI-first أو Adobe-first أو Hybrid أو Manual أو Photography.
- إضافة دليل أسئلة المصمم الذاتية لكل مرحلة.
- إضافة مرجع لقياس الأداء والتعلم بعد النشر.
- الحفاظ على فلسفة المهارة الأصلية: الفكرة قبل القالب، والمراجع للتعلم لا للنسخ، والتصميم الجرافيكي ليس واجهة UI افتراضيًا.
- الحفاظ على دقة النص العربي وسلامة الشعارات والمكونات المستقلة.

## محتويات الحزمة

- SKILL.md — التعليمات الأساسية وسير العمل.
- CHANGELOG.md — سجل التحديثات.
- SOURCE_NOTES.md — المصادر وقرارات المعمارية.
- CHATGPT_PROJECT_INSTRUCTIONS.md — تعليمات جاهزة لإضافتها إلى ChatGPT Project.
- references/artistic-intelligence.md — الذكاء الفني.
- references/brainstorming.md — العصف الذهني وتطوير الأفكار.
- references/art-direction.md — التوجيه الفني.
- references/graphic-design-foundations.md — أساسيات التصميم الجرافيكي.
- references/composition-layout.md — التكوين والتخطيط.
- references/typography.md — Typography.
- references/color-imagery.md — اللون والصورة.
- references/visual-storytelling.md — السرد البصري.
- references/anti-ai-slop.md — مقاومة مخرجات AI النمطية.
- references/reference-analysis.md — تحليل المراجع.
- references/component-integrity.md — سلامة النصوص والمكونات المستقلة.
- references/design-critique.md — نقد التصميم.
- references/production-delivery.md — التنفيذ والتسليم.
- references/decision-log.md — سجل القرارات.
- references/marketing-led-design.md — التفكير التسويقي والجمهور والرسالة.
- references/ai-adobe-workflow.md — مسار AI وAdobe.
- references/phase-self-questions.md — أسئلة المصمم الذاتية.
- references/creative-brief-template.md — قالب Brief.
- references/performance-learning.md — قياس الأداء والتعلم.
- evals/ — سيناريوهات اختبار السلوك.
- scripts/validate_package.py — التحقق البنيوي من الحزمة.

## طريقة الاستخدام

1. ضع مجلد artist-graphic-designer داخل مجلد المهارات الذي يقرأه نظام الوكيل أو المساعد.
2. احتفظ باسم SKILL.md وبنية references كما هي حتى تعمل الإحالات.
3. اجعل النظام يقرأ SKILL.md في مهام التصميم والإبداع البصري.
4. يقرأ النموذج المراجع المناسبة فقط حسب نوع المهمة.
5. استخدم evals/evals.json لاختبار المهارة، ثم قارن النتائج مع المهارة وبدونها.
6. شغّل أداة التحقق من جذر المجلد بالأمر: python scripts/validate_package.py.

## كيف تطلب من ChatGPT اتباعها؟

أضف محتوى CHATGPT_PROJECT_INSTRUCTIONS.md إلى تعليمات المشروع، أو استخدم العبارة التالية في المحادثة:

"استخدم artist-graphic-designer واتبع Marketing-led Creative Design OS. خلّينا نمشي مرحلة مرحلة باستخدام أسئلة المصمم الذاتية."

إذا كنت تريد أن تتعلم التفكير بنفسك، أضف:
"لا تجاوب بدلًا مني على كل شيء. اسألني سؤالًا واحدًا في المرحلة الحالية، راجع إجابتي، وساعدني أكتشف الثغرات قبل الانتقال."

## النطاق

المهارة عامة وليست متخصصة في الطعام أو قطاع بعينه. يمكن ربطها بمهارات قطاعية أو أدوات تنفيذ متخصصة دون جعلها تتحكم في التفكير الفني العام. إذا كان العمل فنًا شخصيًا غير تسويقي، لا تفرض عليه Funnel أو KPIs.

## المبدأ الحاكم

**الاستراتيجية تحدد ما الذي يجب أن نقوله، والفكرة تحدد كيف نقوله، والتوجيه الفني يحوّلها إلى لغة بصرية، والتصميم يحقق التواصل، والحرفية تضمن الجودة، والقياس يساعدنا على التطور.**

## الحالة

الإصدار 0.4.0 يضيف الإطار التسويقي والإنتاج الهجين AI + Adobe وأسئلة المصمم الذاتية وقياس الأداء. يحتوي على 19 مرجعًا متخصصًا و15 سيناريو تقييم. ملفات التقييم تحدد السلوك المتوقع، لكنها لا تثبت وحدها تحسن الجودة؛ يجب تشغيلها ومراجعة النتائج فعليًا.
