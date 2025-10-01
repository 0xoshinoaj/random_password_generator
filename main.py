import random
import string
from config import PASSWORD_CONFIG

def get_allowed_chars():
    """獲取允許使用的字符集"""
    chars = ''
    if PASSWORD_CONFIG['use_uppercase']:
        chars += string.ascii_uppercase
    if PASSWORD_CONFIG['use_lowercase']:
        chars += string.ascii_lowercase
    if PASSWORD_CONFIG['use_digits']:
        chars += string.digits
    if PASSWORD_CONFIG['use_symbols']:
        chars += PASSWORD_CONFIG['symbols']
    return chars

def get_first_char_set():
    """獲取允許的首字符集"""
    chars = ''
    rules = PASSWORD_CONFIG['first_char_rules']
    
    if rules['allow_uppercase']:
        chars += string.ascii_uppercase
    if rules['allow_lowercase']:
        chars += string.ascii_lowercase
    if rules['allow_digits']:
        chars += string.digits
    if rules['allow_symbols']:
        chars += PASSWORD_CONFIG['symbols']
    return chars

def generate_password():
    """生成密碼"""
    if PASSWORD_CONFIG['length'] < 1:
        raise ValueError("密碼長度必須大於0")
    
    # 獲取字符集
    all_chars = get_allowed_chars()
    first_chars = get_first_char_set()
    
    if not all_chars or not first_chars:
        raise ValueError("沒有可用的字符集")
    
    # 計算需要多少必要字符
    required_chars = []
    
    if PASSWORD_CONFIG['use_uppercase']:
        required_chars.append(random.choice(string.ascii_uppercase))
    if PASSWORD_CONFIG['use_lowercase']:
        required_chars.append(random.choice(string.ascii_lowercase))
    if PASSWORD_CONFIG['use_digits']:
        required_chars.append(random.choice(string.digits))
    if PASSWORD_CONFIG['use_symbols']:
        required_chars.append(random.choice(PASSWORD_CONFIG['symbols']))
    
    if len(required_chars) > PASSWORD_CONFIG['length']:
        raise ValueError("密碼長度太短，無法包含所有必要字符類型")
    
    # 生成首字符（從允許的首字符中選擇）
    password_chars = [random.choice(first_chars)]
    
    # 添加必要字符（排除已用作首字符的）
    random.shuffle(required_chars)  # 隨機打亂必要字符順序
    for char in required_chars:
        if len(password_chars) < PASSWORD_CONFIG['length']:
            password_chars.append(char)
    
    # 填充剩餘長度
    remaining_length = PASSWORD_CONFIG['length'] - len(password_chars)
    password_chars.extend(random.choice(all_chars) for _ in range(remaining_length))
    
    # 隨機打亂除了第一個字符以外的所有字符
    rest_chars = password_chars[1:]
    random.shuffle(rest_chars)
    password_chars[1:] = rest_chars
    
    return ''.join(password_chars)

def main():
    try:
        # 生成多組密碼
        passwords = [generate_password() for _ in range(PASSWORD_CONFIG['password_count'])]
        
        # 將密碼寫入文件，每行一個密碼
        with open('random_password.txt', 'w') as f:
            for password in passwords:
                f.write(f"{password}\n")
        
        print(f"密碼已生成並保存到 random_password.txt")
        print("\n生成的密碼為:")
        for password in passwords:
            print(password)
            
    except Exception as e:
        print(f"錯誤: {str(e)}")

if __name__ == '__main__':
    main() 