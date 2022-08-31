%global _empty_manifest_terminate_build 0
Name:		python-pyTelegramBotAPI
Version:	4.7.0
Release:	1
Summary:	Python Telegram bot api.
License:	GPL2
URL:		https://github.com/eternnoir/pyTelegramBotAPI
Source0:	https://files.pythonhosted.org/packages/76/f8/ab1e065ceef0b0f72b25f357f04332a8f8afb1929b3c14bc08d5eb869355/pyTelegramBotAPI-4.7.0.tar.gz
BuildArch:	noarch

%description
A simple, but extensible Python implementation for the Telegram Bot API.
%package -n python3-pyTelegramBotAPI
Summary:	Python Telegram bot api.
Provides:	python-pyTelegramBotAPI
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-pyTelegramBotAPI
A simple, but extensible Python implementation for the Telegram Bot API.
%package help
Summary:	Development documents and examples for pyTelegramBotAPI
Provides:	python3-pyTelegramBotAPI-doc
%description help
Development documents and examples for pyTelegramBotAPI
%prep
%autosetup -n pyTelegramBotAPI-4.7.0

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-pyTelegramBotAPI -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Wed Aug 31 2022 hkgy <kaguyahatu@outlook.com> - 4.7.0-1
- Update to 4.7.0

* Tue Jul 05 2022 hkgy <kaguyahatu@outlook.com> - 4.6.0-1
- Upgrade version to 4.6.0

* Sun May 23 2021 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
