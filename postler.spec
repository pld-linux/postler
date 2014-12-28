Summary:	A super sexy, ultra simple desktop mail client built in vala
#Summary(pl.UTF-8):	-
Name:		postler
Version:	0.1.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Mail
Source0:	http://archive.xfce.org/src/apps/postler/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	02e502c9f4a4b92e4ace32d9e268f06d
URL:		https://launchpad.net/postler
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.26
BuildRequires:	gtk+2-devel >= 2:2.18
BuildRequires:	gtk-webkit-devel >= 1.1.18
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libcanberra-devel
BuildRequires:	libindicate-devel
BuildRequires:	libnotify-devel
BuildRequires:	libunique-devel >= 0.9
BuildRequires:	lynx
BuildRequires:	msmtp
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	vala
Requires:	msmtp
#Suggests:	Dexter
#Suggests:	lynx
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Postler aims to be easy, simple, clean, beautiful, and automagic. It
handles IMAP beautifully, and provides the user with smart, sensible
defaults.

#%description -l pl.UTF-8

%prep
%setup -q

%build
./waf configure \
	--prefix=/usr

./waf build

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--prefix=/usr \
	--destdir=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/postler
%attr(755,root,root) %{_bindir}/postler-mbsync
%{_desktopdir}/postler.desktop
%{_iconsdir}/hicolor/*/apps/internet-mail.*
