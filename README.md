# andreaw-rest

### [Proje için Python Sanal Ortamın (Virtual Environment) ve Bağımlılıkların Yüklenmesi](#virtualenv)

1. Python3 için pip güncellemesi ve `virtualenv` paketinin kurulması

```
  sudo -H pip3 install --upgrade pip
  sudo -H pip3 install virtualenv
```

**Not:** *"locale.Error: unsupported locale setting"* hatası için çözüm:

```
  export LC_ALL="en_US.UTF-8"
```

2. Örnek bir Django projesi GitHub'dan kopyalanıyor.

```
  git clone https://github.com/barissaslan/eventhub.git
```

3. Proje dizinine geçme ve `venv` adlı Sanal Python Ortamının oluşturulması

```
  cd eventhub
  virtualenv venv
```

4. Sanal Ortamın aktif edilmesi

```
  source venv/bin/activate
```

5. Proje bağımlılıklarının yüklenmesi

```
  pip install -r requirements.txt
```
