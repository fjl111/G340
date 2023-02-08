import requests
import json
import smtplib
import datetime
import time

# Email information
gmail_user = 'aombutton@gmail.com'
gmail_password = 'tthcuzqsphggahse'
sent_from = gmail_user
to = ['katmcg01@outlook.com', 'isabhsia@gmail.com', 'cassidyh1653@gmail.com', 'flaudati04@gmail.com']
email_text = ''

# IoT information
payload = {'X-AIO-Key': 'aio_shff381Fm5UORAhaoCzf9xY8dlT7'}
url = 'https://io.adafruit.com/api/v2/aom_cloud/feeds/cloud.feed-a'



def construct_email(subject, body):
    global email_text
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)


def send_email():
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print("Email sent successfully with message: ")
        print(email_text)
    except Exception as ex:
        print("Something went wrong…", ex)


def get_new_val():
    # Get new data from the IoT
    r = requests.get(url, params=payload)
    try:
        data = json.loads(r.content.decode())
        last_val_string = data['last_value']
        if last_val_string == 'HIGH':
            return 1
        elif last_val_string == 'LOW':
            return 0
        else:
            print('Error, wrong value')
        # print(data['last_value'])
    except:
        print('error thrown')
        print(r)



def get_full_code():
    all_vals = '1'
    end_time = datetime.datetime.now() + datetime.timedelta(0, 40)
    i = 0

    # While it is possible for new values to be sent in, read them
    while datetime.datetime.now() < end_time:
        new_val = get_new_val()
        # Make sure new value is not the same as the old one
        if str(new_val) != all_vals[i] and new_val != None:
            all_vals += str(new_val)
            i += 1
        time.sleep(2)
    # Once all values are read, send them back to the main
    print(all_vals)
    return all_vals


def translate_code(code):
    print('Translating')
    # Hailey 3
    # Bella 6
    # Katie 1
    # Jack 2
    # Samsher 4
    # Dr. Samosky 5
    if code == '10': #3
        return 'Hailey'
    elif code == '1010': #2
        return 'Jack'
    elif code == '101010': #1
        return 'Katie'
    elif code == '10101010': #4
        return 'Samsher'
    elif code == '1010101010': #5
        return 'Dr. Samosky'
    elif code == '101010101010': #6
        return 'Bella'
    else:
        return 'error'


if __name__ == '__main__':
    while True:
        last_val = get_new_val()
        if last_val == 1:
            print('Getting Code')
            person = translate_code(get_full_code())
            construct_email('%s has arrived to G34!!' % person,
                            'Your teammate, %s, has checked into Room G34. Send them a text or perhaps, meet them there!'
                            % person)
            send_email()
            time.sleep(2.5)
