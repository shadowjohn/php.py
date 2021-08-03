# php.py
Python Implementation of PHP Functions

Let PHPers coding with python seamlessly. Additional packages like re and beautifulsoup make your life easier, just like coding in PHP!

<pre>
Newest version:
  1.4
  
License:
  LGPLv3

Requirements:
  python -m pip install --upgrade pip
  require
  requests
  BeautifulSoup4

Usage:
  Step 1:
    copy php.py to your project
  Step 2:
    import php
    my = php.kit()
    print(my.date('Y-m-d'));
    
    or
    
    import imp
    import os
    import sys
    PWD = os.path.dirname(os.path.abspath(__file__));   
    php = imp.load_source('module', PWD+"\\lib\\php.py")
    my = php.kit() 
    print(my.date('Y-m-d'));
    
</pre>

Changes:
* Tus Aug 03 2021 (FeatherMountain (https://3wa.tw)) - V1.4
- Fix mainname()
- Fix pwd()
- Remove old version

* Thu Sep 21 2016 (FeatherMountain (http://3wa.tw)) - V1.3
- Fix method urlencode.
- Fix file_get_contents for get mode only.
 

* Thu Sep 12 2016 (FeatherMountain (http://3wa.tw)) - V1.2
- Fix file_get_contents_post headers initial.
- Add method urlencode.
- Add method python_version.

* Thu Sep 01 2016 (FeatherMountain (http://3wa.tw)) - V1.1
- Fix file_get_contents_post retry times.

* Sun Aug 28 2016 (FeatherMountain (http://3wa.tw)) - V1.0
- First release
