# میزبانی رایگان اذان‌ها روی گیت‌هاب (بدون سرور، بدون هزینه)

## یک‌بار راه‌اندازی (حدود ۱۰ دقیقه)
1. در github.com حساب رایگان بسازید.
2. دکمهٔ New repository: نام مثلاً `azan-library`، حالت **Public**، سپس Create.
3. در صفحهٔ مخزن: Add file ← Upload files. **همهٔ محتویات همین پوشه** (شامل پوشهٔ `.github`، پوشهٔ `azan` و فایل `make_catalog.py`) را بکشید و Commit کنید.
   - اگر پوشهٔ `.github` با کشیدن آپلود نشد، در گیت‌هاب Add file ← Create new file بزنید، نام فایل را `.github/workflows/catalog.yml` بنویسید و محتوای فایل را کپی کنید.
4. Settings ← Pages ← Source: Deploy from a branch ← شاخهٔ `main` و پوشهٔ `/ (root)` ← Save.
5. Settings ← Actions ← General ← Workflow permissions: **Read and write permissions** را بزنید و Save کنید.

## افزودن اذان جدید
1. وارد پوشهٔ `azan` در مخزن شوید ← Add file ← Upload files ← فایل‌های صوتی را بکشید ← Commit.
2. حدود یک دقیقه صبر کنید؛ فایل `azan/catalog.json` خودکار ساخته می‌شود.
3. برای حذف اذان، فایلش را از پوشه پاک کنید.

## اتصال به برنامه (فقط یک‌بار)
در `Sounds.kt` مقدار زیر را عوض کنید (به‌جای `USERNAME` و `azan-library` نام خودتان را بگذارید):

    const val CATALOG_URL = "https://USERNAME.github.io/azan-library/azan/catalog.json"

بعد از انتشار برنامه، دیگر هر اذان جدیدی که آپلود کنید، بدون به‌روزرسانی برنامه در دسترس همه می‌گذارد.

## محدودیت‌ها
- حجم کل سایت حداکثر ۱ گیگابایت و مصرف ترافیک حدود ۱۰۰ گیگابایت در ماه (محدودیت نرم).
- هر اذان حدود ۳ مگابایت و هر کاربر یک‌بار دانلود می‌کند (فایل روی گوشی می‌ماند)، پس حدود ۳۰ هزار دانلود در ماه جا دارد.
- فقط محتوایی بگذارید که حق انتشارش را دارید.
