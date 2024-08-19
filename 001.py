import datetime
import smtplib
from email.mime.text import MIMEText


# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Function to find prime numbers up to a given limit
def find_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes


# Function to send an email
def send_email(subject, body, to_email):
    from_email = 'your_email@example.com'
    password = 'your_email_password'
    a

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())


# Main function
def main():
    today = datetime.date.today()
    primes = find_primes(931)  # Set the limit according to your requirement
    prime_dates = [today + datetime.timedelta(days=p) for p in primes]

    for prime_date in prime_dates:
        print(f"Prime Numbered Day: {prime_date}")
        # Send reminder email
        subject = 'Reminder: Prime Numbered Day'
        body = f"Today is a prime-numbered day: {prime_date}"
        send_email(subject, body, 'recipient@example.com')


if __name__ == "__main__":
    main()