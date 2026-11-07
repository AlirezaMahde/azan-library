#!/usr/bin/env python3
"""
ساخت catalog.json از یک پوشه فایل صوتی؛ بدون ربات، بدون توکن، بدون اینترنت.

روش کار:
  ۱) فایل‌های اذان را از کانال بله دانلود کنید و داخل یک پوشه بگذارید.
  ۲) این دستور را اجرا کنید:
        python make_catalog.py  پوشه  https://your-domain.com/azan
  ۳) محتوای کل پوشه (فایل‌ها + catalog.json) را روی هاست HTTPS آپلود کنید.
  ۴) آدرس https://your-domain.com/azan/catalog.json را در Config.CATALOG_URL بگذارید.

نام فایل = عنوان اذان در برنامه (مثلاً «اذان مکه - مؤذن.mp3»).
"""
import hashlib
import json
import os
import re
import sys
import urllib.parse

EXT = {".mp3", ".ogg", ".m4a", ".aac", ".wav"}
MAX_BYTES = 20 * 1024 * 1024  # سقف مجاز برنامه


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def main(folder, base):
    if not base.startswith("https://"):
        sys.exit("آدرس پایه باید با https:// شروع شود.")
    items, used = [], set()
    for i, fn in enumerate(sorted(os.listdir(folder)), 1):
        name, ext = os.path.splitext(fn)
        path = os.path.join(folder, fn)
        if ext.lower() not in EXT or not os.path.isfile(path):
            continue
        size = os.path.getsize(path)
        if size > MAX_BYTES:
            print(f"رد شد (بیش از ۲۰ مگابایت): {fn}")
            continue
        sid = re.sub(r"[^a-z0-9_-]+", "_", name.lower()).strip("_") or f"azan_{i}"
        while sid in used:
            sid += "_x"
        used.add(sid)
        items.append({
            "id": sid,
            "title": name.replace("_", " ").strip(),
            "artist": "",
            "url": base.rstrip("/") + "/" + urllib.parse.quote(fn),
            "size": size,
            "sha256": sha256(path),
        })
        print(f"✓ {fn}")
    out = os.path.join(folder, "catalog.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"version": 1, "items": items}, f, ensure_ascii=False, indent=2)
    print(f"\n{len(items)} اذان در {out} ثبت شد.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
