# 密碼生成配置
PASSWORD_CONFIG = {
    # 密碼長度
    'length': 15,
    
    # 要生成的密碼數量
    'password_count': 20,
    
    # 字符類型設置
    'use_uppercase': True,    # 使用大寫字母
    'use_lowercase': True,    # 使用小寫字母
    'use_digits': True,      # 使用數字
    'use_symbols': True,     # 使用符號
    
    # 自定義符號集合
    #'symbols': '!@#$%^&*()_+-=[]{}|;:,.<>?',
    'symbols': '!@#$%^&*()<>?',
    
    # 首字符限制
    'first_char_rules': {
        'allow_uppercase': True,   # 預設允許大寫字母開頭
        'allow_lowercase': True,   # 預設允許小寫字母開頭
        'allow_digits': False,     # 預設不允許數字開頭
        'allow_symbols': False     # 預設不允許符號開頭
    }
} 