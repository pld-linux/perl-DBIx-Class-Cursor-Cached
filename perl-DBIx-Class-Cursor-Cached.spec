#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Class-Cursor-Cached
Summary:	DBIx::Class::Cursor::Cached - cursor class with built-in caching support
#Summary(pl.UTF-8):
Name:		perl-DBIx-Class-Cursor-Cached
Version:	1.0.1
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSTROUT/DBIx-Class-Cursor-Cached-%{version}.tar.gz
# Source0-md5:	9cf5f4b1e698e68a524d6a432f4e1c6b
URL:		http://search.cpan.org/dist/DBIx-Class-Cursor-Cached/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Cache-Cache
BuildRequires:	perl-DBIx-Class >= 0.08004
BuildRequires:	perl-Digest-SHA1
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cursor class with built-in caching support.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/DBIx/Class/Cursor
%{perl_vendorlib}/DBIx/Class/Cursor/*.pm
%{_mandir}/man3/*
