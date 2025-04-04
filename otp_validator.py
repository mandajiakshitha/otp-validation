import random

def generate_otp():
    return str(random.randint(100000, 999999))  # Generate 6-digit OTP

def send_otp(email, otp):
    print(f"Simulating sending OTP to {email}...")  
    print(f"Your OTP is: {otp}")  # Normally, you would use an email service here

def get_user_input():
    return input("Enter the OTP received on your email: ").strip()

def verify_otp(generated_otp):
    attempts = 3
    while attempts > 0:
        user_otp = get_user_input()
        if user_otp == generated_otp:
            print("✅ OTP Verified! Access Granted.")
            return True
        else:
            attempts -= 1
            print(f"❌ Incorrect OTP. {attempts} attempts left.")
    
    print("🚫 Access Denied. Too many incorrect attempts.")
    return False

def main():
    email = input("Enter your email: ")  # Get user email
    otp = generate_otp()  # Generate OTP
    send_otp(email, otp)  # Send OTP
    verify_otp(otp)  # Verify OTP

if __name__ == "__main__":
    main()
