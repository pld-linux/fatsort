# TODO:
#	- tests requires mounting filesystem images
#
# Conditional build:
%bcond_with	tests		# build with tests
#
Summary:	Utility that sorts FAT12, FAT16 and FAT32 partition
Name:		fatsort
Version:	1.3.365
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://downloads.sourceforge.net/fatsort/%{name}-%{version}.tar.gz
# Source0-md5:	f1232f40eba6ee9362acd9f0d5209dcf
URL:		http://fatsort.sourceforge.net
%{?with_tests:BuildRequires:	bbe}
%{?with_tests:BuildRequires:	dosfstools}
BuildRequires:	help2man
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FATSort is a C utility that sorts FAT12, FAT16 and FAT32 partitions.
It even can handle long file name entries. It was developed because I
wanted to sort my MP3 files on my MP3 hardware player. Unfortunetly,
there was no utility out there so far, so I had to write it myself.
FATSort reads the boot sector and sorts the directory structure
recursively.

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
%doc CHANGES README
%attr(755,root,root) %{_sbindir}/fatsort
%{_mandir}/man1/fatsort.1*
