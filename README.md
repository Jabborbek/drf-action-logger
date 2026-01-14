# DRF Action Logger
## 📌 Muhim eslatma

Hozircha ushbu loyiha **PyPI orqali tarqatilmaydi** va `pip install` qilish imkoniyati yo‘q.

Bu loyiha:
- tajriba (experimental) holatida
- real loyihalarda sinab ko‘rish uchun
- ochiq kodli (open-source) tarzda taqdim etilgan

Agar loyiha foydali bo‘lsa, GitHub’da ⭐ yulduzcha qo‘yib qo‘llab-quvvatlasangiz,
kelgusida uni **rasmiy PyPI paketi** sifatida chiqarish rejalashtirilgan.

---

## 🧩 Qanday foydalaniladi?

Hozircha loyihadan foydalanish uchun uni **GitHub orqali clone qilib** olishingiz mumkin:

```bash
git clone https://github.com/Jabborbek/drf-action-logger.git
````

So‘ngra loyiha ichidagi `action_logs` app’ini:

* o‘z Django loyihangizga qo‘shishingiz
* `INSTALLED_APPS` ga kiritishingiz
* middleware sifatida ulab ishlatishingiz

mumkin.

---

## ⚙️ Sozlash (settings.py)

Logger to‘g‘ri ishlashi uchun **settings.py** faylingizga ham kerakli sozlamalarni qo‘shishingiz zarur.

Quyidagi sozlamalarni loyiha bilan birga berilgan **example** asosida
o‘z `settings.py` faylingizga moslab qo‘shing:

```python
INSTALLED_APPS = [
    ...
    'action_logs',
]

MIDDLEWARE = [
    ...
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'action_logs.middleware.api_logger_middleware.APILoggerMiddleware',
]

DRF_API_LOGGER_DATABASE = True
DRF_API_LOGGER_SIGNAL = False

```

⚠️ Eslatma: Middleware **AuthenticationMiddleware dan keyin** qo‘shilishi tavsiya etiladi.

---

## 🛠 Moslashtirish (Customization)

Ushbu loyiha:

* to‘liq ochiq kodli
* istalgancha o‘zgartirish kiritish mumkin
* o‘zingizga moslab sozlashga ruxsat etiladi

Agar sizga qo‘shimcha funksiyalar kerak bo‘lsa:

* kodni bemalol tahrirlashingiz
* yangi imkoniyatlar qo‘shishingiz
* o‘z loyihangiz ehtiyojiga moslab olishingiz mumkin

---

## ⭐ Qo‘llab-quvvatlash

Agar loyiha sizga foydali bo‘lsa:

* GitHub’da ⭐ yulduzcha qo‘yish
* fikr-mulohaza bildirish
* takliflar berish

katta yordam bo‘ladi.

Yetarli qiziqish bo‘lsa, loyiha rasmiy **PyPI paketi** sifatida chiqariladi.

---

## ☕ Loyihani qo‘llab-quvvatlash

Agar ushbu loyiha sizga foydali bo‘lgan bo‘lsa va ish jarayoningizni yengillashtirgan bo‘lsa,
bu men uchun katta motivatsiya bo‘ladi 🙏

Xavfsizlik va maxfiylik sababli karta ma’lumotlari ochiq e’lon qilinmaydi.

Agar loyihani qo‘llab-quvvatlamoqchi bo‘lsangiz, iltimos:

* **Telegram** yoki
* **Elektron pochta**

orqali bog‘laning — kerakli ma’lumotlarni shaxsan ulashaman.

### 📬 Aloqa uchun:

* **Email:** [JabborbekQobilov@gmail.com](mailto:JabborbekQobilov@gmail.com)
* **Telegram:** @JabborbekQobilov

Sizning qo‘llab-quvvatlashingiz ushbu open-source loyihaning rivojlanishiga yordam beradi.

## **Katta rahmat! 🙌**
