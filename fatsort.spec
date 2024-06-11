# TODO:
#	- tests requires mounting filesystem images
#
# Conditional build:
%bcond_with	tests	# functional tests
#
Summary:	Utility that sorts FAT12, FAT16 and FAT32 partition
Summary(pl.UTF-8):	Narzędzie do sortowania partycji FAT12, FAT16 i FAT32
Name:		fatsort
Version:	1.6.5.640
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://downloads.sourceforge.net/fatsort/%{name}-%{version}.tar.xz
# Source0-md5:	5c545634fe15e6cf44efc847b631718e
URL:		https://fatsort.sourceforge.io/
%{?with_tests:BuildRequires:	bbe}
%{?with_tests:BuildRequires:	dosfstools}
BuildRequires:	help2man
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FATSort is a C utility that sorts FAT12, FAT16 and FAT32 partitions.
It even can handle long file name entries. It was developed because I
wanted to sort my MP3 files on my MP3 hardware player. Unfortunetly,
there was no utility out there so far, so I had to write it myself.
FATSort reads the boot sector and sorts the directory structure
recursively.

%description -l pl.UTF-8
FATSort to narzędzie w C do sortowania partycji FAT12, FAT16 i FAT32.
Potrafi obsłużyć wpisy długich nazw plików. Powstał z potrzeby
posortowania plików MP3 dla sprzętowego odtwarzacza, kiedy nie było
jeszcze takiego narzędzia. FATSort czyta sektor rozruchowy i sortuje
rekurencyjnie strukturę katalogów.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%{?with_tests:%{__make} tests}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	SBINDIR=%{_sbindir} \
	MANDIR=%{_mandir}/man1 \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md
%attr(755,root,root) %{_sbindir}/fatsort
%{_mandir}/man1/fatsort.1*
