package-verify
==============

Package verification tool which will be renamed at some point.


Usage
-----
```
usage: package-verify [-h] [-q] [-V {devspec}] manifest

positional arguments:
  manifest              The manifest file to validate.

optional arguments:
  -h, --help            show this help message and exit
  -q, --quiet           Goes silent. Success/failure is only noted in the
                        return code.
  -V {devspec}, --validator {devspec}
                        Select a specific validator to use.
```

Example Output
--------------
*Pass Examples*
```
$ package-verify pass.json 
$ echo $?
0
$
```

```
$ package-verify -q pass.json 
$ echo $?
0
$
```

*Failure Examples*
```
$ package-verify fail.json 
E: name is missing
E: files is missing
$ echo $?
1
$
```

```
$ package-verify -q fail.json 
$ echo $?
1
$
```


Making a Validator
------------------
To make a validator follow these rules:

* subclass package\_verify.validator.\_Validator
* name the subclass *Validator*
* implement the validate method
* place the file in package\_verify.validator.validators so it can be found for listing and loading

```python
# filename: testvalidator.py

from package_verify.validator import error, _Validator


class Validator(_Validator):

    def validate(self, data):
        """
        Validates input data.

        :param str data: String of info to validate.
        :raises WrongFormatError: if the format is not useable
        :rtype: tuple
        :returns: Warnings and errors
        """
        # Do stuff here
        return (warnings_list, errors_list)
```
