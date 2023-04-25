# Attacks

This folder contains all the scripts required for different attack techniques for cracking passwords in the Password Cracker project.

## Dictionary Attack
The dictionary attack script (dictionary_attack.py) uses a wordlist of common passwords to crack a given password. To use this script, you need to specify the path to the wordlist and the password hash you want to crack.

### Usage
``` python
python dictionary_attack.py -w <path to wordlist> -p <password hash>
```

## Brute Force Attack
The brute force attack script (brute_force_attack.py) tries all possible combinations of characters to crack a given password. To use this script, you need to specify the minimum and maximum length of the password, the character set to use for the attack, and the password hash you want to crack.

### Usage
``` python
python brute_force_attack.py -min <minimum password length> -max <maximum password length> -c <character set> -p <password hash>
```

## Hybrid Attack
The hybrid attack script (hybrid_attack.py) combines the dictionary attack and brute force attack techniques to crack a given password. To use this script, you need to specify the path to the wordlist, the minimum and maximum length of the password, the character set to use for the attack, and the password hash you want to crack.

### Usage
``` python
python hybrid_attack.py -w <path to wordlist> -min <minimum password length> -max <maximum password length> -c <character set> -p <password hash>
```

## Note
Please note that this project is created for educational and security testing purposes only. Do not use it for any illegal activities. The developers of this project are not responsible for any misuse or damage caused by using this project.

## Contributing
Contributions are welcome and encouraged! If you find any issues or have any suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. Please see the LICENSE file for more information.
