#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-asv
Version  : 0.5.1
Release  : 18
URL      : https://files.pythonhosted.org/packages/5b/e4/f4af30aa6e75c12832f3d61cd07610510e2e47aaa1547513f4a51dd335b1/asv-0.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/5b/e4/f4af30aa6e75c12832f3d61cd07610510e2e47aaa1547513f4a51dd335b1/asv-0.5.1.tar.gz
Summary  : Airspeed Velocity: A simple Python history benchmarking tool
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-asv-bin = %{version}-%{release}
Requires: pypi-asv-license = %{version}-%{release}
Requires: pypi-asv-python = %{version}-%{release}
Requires: pypi-asv-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=================
        
        **airspeed velocity** (``asv``) is a tool for benchmarking Python
        packages over their lifetime.
        
        It is primarily designed to benchmark a single project over its
        lifetime using a given suite of benchmarks.  The results are displayed
        in an interactive web frontend that requires only a basic static
        webserver to host.

%package bin
Summary: bin components for the pypi-asv package.
Group: Binaries
Requires: pypi-asv-license = %{version}-%{release}

%description bin
bin components for the pypi-asv package.


%package license
Summary: license components for the pypi-asv package.
Group: Default

%description license
license components for the pypi-asv package.


%package python
Summary: python components for the pypi-asv package.
Group: Default
Requires: pypi-asv-python3 = %{version}-%{release}

%description python
python components for the pypi-asv package.


%package python3
Summary: python3 components for the pypi-asv package.
Group: Default
Requires: python3-core
Provides: pypi(asv)
Requires: pypi(six)

%description python3
python3 components for the pypi-asv package.


%prep
%setup -q -n asv-0.5.1
cd %{_builddir}/asv-0.5.1
pushd ..
cp -a asv-0.5.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685562388
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-asv
cp %{_builddir}/asv-%{version}/LICENSE.rst %{buildroot}/usr/share/package-licenses/pypi-asv/8565420f58601d5de7f1124e5e20c2f6ab1a6a6b || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/asv

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-asv/8565420f58601d5de7f1124e5e20c2f6ab1a6a6b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
