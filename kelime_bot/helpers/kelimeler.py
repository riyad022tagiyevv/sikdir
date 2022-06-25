import random

kelimeler = ["gözəl ","bilmək ","sual","sağalmaq ","getmək","zaman","su","yarmaq","dəli","görmək",

             "yenidən", "çox", "fakt", "pul", "oynamaq", "çiçək", "şəhər", "yüksəlmək", "döyüş", "varlıq", "etmək",

             "güvən", "lazım", "müalicə", "bir", "rahat", "soyuq", "orası", "kitab", "paylaşmaq", "hesap", "bədən",

             "torpaq", "üzəri", "sistem", "xoş", "çəkilmək", "texnik", "yaxınlaşmaq", "il", "tarix", "kəsir", "bacı",

             "incə", "deyər", "oyda", "qarşılıql","vermək", "sahib", "artıq", "kişi", "diyar", "dönəm", "yenə", "bunlar",

             "kitab", "xəta", "tapmaq", "siz", "dövlət", "qabaq", "enerji", "baxmaq", "xiyar", "oyun", "baş", "başlamaq",

             "tutmaq", "birbiri", "heçbir", "yatmaq", "su", "ürək", "hal", "doğru", "orta", "başqa", "böyük", "etmək",

             "yeni", "çoxlu", "soruşmaq", "onlar", "açmaq", "həmin", "həb", "səs", "ağlamaq", "dəli", "saat", "fəsil",

             'bir', 'veteran', 'olmak', 'bu', 'içki', 'onuncu', 'bibar', 'demək', 'çox', 'yaşıl', 'ana', 'kimi', 'daha', 'almaq',

             'var', 'özün', 'gəlmək', 'ilə', 'vermək', 'baba', 'sonra', 'qədir', 'yer', 'ata', 'insan', 'deyil', 'hər',

             'istəmək', 'ilan', 'çıxmaq', 'görmək', 'gün', 'biz', 'getmkə', 'iş', 'ölüm', 'axtarmaq', 'iki', 'bilmək', 'əl', 'zaman',

             'ya', 'uşaq', 'iki', 'baxmaq', 'işləmək', 'içində', 'böyük', 'yox', 'başlamaq', 'yol', 'düzgün', 'feil', 'siz',

             'söz', 'yaradmaq', 'yaxşı', 'qadın', 'evli', 'demək', 'tapmaq', 'demək', 'göz', 'lazımlı', 'dünya',

             'baş', 'vaxt', 'yan', 'getmək', 'sən', 'onlar', 'yeni', 'öncə', 'başqa', 'hal', 'orta', 'su', 'girmək', 'ölkə',

             'yemək', 'heçnə', 'oxumaq', 'necə', 'bütün', 'qarşı', 'tapmaq', 'evvli', 'yaşamak', 'yuxari', 'güzgü', 'içmək', 'ancaq',

             'kişi', 'bunlar', 'veya', 'ilk', 'göre', 'qabaq', 'son', 'biri', 'şəkil', 'önemli', 'yüz', 'həmin', 'göstərmək', 'etmək',

             'alt', 'gətirmək', 'işlətmək', 'çünkü', 'tərəf', 'kimdi', 'adam', 'onun', 'diğer', 'artıq', 'ütüntə', 'səs', 'hep',

             'doğru', 'dayanmaq', 'qız', 'tüm', 'süd', 'zəng', 'pullu', 'anlamak', 'nanə', 'qoşqar', 'bazar', 'baba', 'hayat',

             'sadece', 'balaca', 'çox', 'bilgi', 'an', 'soruşma', 'bunun', 'öyle', 'yine', 'sağalmaq', 'kəsir', 'eynək', 'diş',

             'ad', 'yəni', 'vaxt', 'dönmek', 'açmak', 'oturmak', 'anlatmak', 'bırakmak', 'həmən', 'saat', 'yaş', 'xəta', 'dövlət',

             'sahib', 'sıra', 'yazmak', 'yüzdə', 'ay', 'atmak', 'tutmaq', 'burun', 'qəza', 'yarı', 'qulaq', 'söz', 'gözəl',

             'sevmek', 'biraz', 'zor', 'çıxmaq', 'suni', 'koymak', 'tək', 'sistem', 'toplu', 'vergi', 'kim', 'incimək', 'gənc',

             'kapı', 'kitab', 'üstün', 'burada', 'gecə', 'alan', 'bərbər', 'işdə', 'gizli', 'uzun', 'hiçbir', 'bugün', 'fokus',

             'dost', 'soyad', 'aile', 'üç', 'okumaq','kişi', 'hərkəs', 'güc', 'bəlmək', 'doğru', 'tam', 'gecə', 'Riyad',

             'çevrə', 'köhnə', 'zəng', 'yaşma', 'əhali', 'yaxın', 'yol', 'bəy', 'tarix', 'özellik', 'bölüm', 'şəxsi', 'ağıl',

             'kimsə', 'pak', 'baş', 'gerek', 'yaxın', 'anlamaq', 'yuxarı', 'banka', 'kriz', 'ayak', 'daşımaq', 'geri', 'toplu',

             'maşın', 'maddə', 'türk', 'qəlyan', 'görüldü', 'hava', 'sayı', 'farklı', 'qrup', 'otaq', 'bacı', 'dolmaq', 'xəbər',

             'allah', 'ayrıca', 'gələn', 'çin', 'sual', 'arxa', 'qazanmaq', 'yazı', 'dərs', 'açıq', 'öyrənmək', 'sürmək',

             'dil', 'şirket', 'qaynaq', 'bitmək', 'program', 'devametmek', 'hareket', 'rəng', 'açılmaq', 'hak', 'inanmaq',

             'çalmaq', 'acı', 'parça', 'qazet', 'yaratmaq', 'yaxşı', 'dəyər', 'tanımaq', 'kley', 'doxdur', 'gəlir',

             'hərbiçi', 'zəfər', 'bölge', 'kino', 'üzere', 'satıcı', 'zolaq', 'telefon', 'aydın', 'dəniz', 'ikinci',

             'qalxmaq', 'düzgün', 'qar', 'gəlir', 'keçən', 'boyun', 'düşüncə', 'milyon', 'oynamaq', 'dəyişmək', 'tütün',

             'yaratmaq', 'xal', 'fikir', 'keçmək', 'söyüş', 'qurmaq', 'fakt', 'buna', 'rəsim', 'ışıq', 'içmək',

             'xanım', 'xəstə', 'ehtiyac', 'nöktə', 'yönlü', 'xəta', 'oyun', 'artmak', 'yenidən', 'şar', 'qısa', 'asta',

             'şan', 'qan', 'əsla', 'ağıl', 'orada', 'diqqət', 'uzaq', 'bilgisayar', 'gələcək', 'görünmək',

             'şəkil', 'oğul', 'dinləmək', 'uyğun', 'manat', 'passiv', 'dəqiq', 'unutmaq', 'cəld', 'eynək', 'pis',

             'maşın', 'ağız', 'dünya', 'uygulamak', 'xala', 'örnek', 'azlıq', 'baxmaq', 'dərəcə', 'mümkün', 'dondurma',

             'divar', 'onsuz', 'sənə', 'ana', 'xəstəlik', 'öğrenci', 'televizor', 'kino', 'stul', 'ölmək', 'taksi', 'üst',

             'baş', 'mahnı', 'sevgi', 'enerji', 'üniversite', 'spor', 'türlü', 'cansız', 'balta', 'soyuducu', 'ölüm',

             'dərdli', 'sağlam', 'inək', 'banan', 'hissetmek', 'nənə', 'sabah', 'internet', 'texnik', 'dondurma',

             'mərkəz', 'orta', 'yerinə', 'düz', 'kənd', 'yorulmaq', 'aşağı', 'cavab', 'yatmaq', 'torpaq', '', 'axşam',

             'sarı', 'götürmek', 'qatılmaq', 'yoxsul', 'qurmaq', 'ödəmək', 'sanki', 'kan', 'hasta', 'şehir', 'inmek',

             'qara', 'qaynaq', 'həftə', 'lənpə', 'hesab', 'otomobil', 'başqa', 'davranış', 'mutfak', 'kent', 'bazen',

             'vacib', 'ayrı', 'qiymət', 'hakkında', 'qaldırmaq', 'kola', 'tək', 'hazırlamaq', 'cam', 'sonunda', 'yavaş',

             'lazım', 'dəyər', 'arvad', 'yallı', 'varlı', 'tar', 'arı', 'təkcə', 'satış', 'içeri', 'doğal', 'sahipolmak',

             'şənlik', 'acı', 'xeyir', 'qorumaq', 'qat', 'ekonomi', 'genel', 'bildirmək', 'fotoğraf', 'hayvan', 'savaş',

             'yumurta', 'alma', 'plan', 'istəmək', 'kərim', 'kriz', 'birlik',

             'qapanmaq'

             ]

def kelime_sec():

    return random.choice(kelimeler)
