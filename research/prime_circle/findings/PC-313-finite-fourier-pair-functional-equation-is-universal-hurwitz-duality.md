# PC-313 — finite-Fourier pair functional equation is universal Hurwitz duality

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the minimal vector-valued functional-equation escape left open by PC-312 after the canonical mixed-conductor Prime-Circle packet has already been compressed to one periodic coefficient sequence.

PC-312 proves that the canonical coefficient `d` forced by the PC-311 two-prime Poisson pairing is not a finite-Fourier eigenvector, so its Dirichlet series does not close on itself under a scalar degree-one Riemann-type functional equation. The most immediate surviving repair was to retain both `d` and its normalized finite Fourier transform `F_N d`, allowing a two-component functional equation rather than forcing scalar self-duality.

That repair is exact but completely universal. For **every even periodic coefficient sequence**, independently of any Prime-Circle arithmetic, the standard Hurwitz-zeta transformation exchanges the completed Dirichlet series of `d` with that of `F_N d`. The resulting two-component functional equation has the constant swap matrix. Since `F_N^2=1` on the even subspace, diagonalizing that matrix gives precisely the manually Fourier-symmetrized coefficients `d+F_Nd` and `d-F_Nd`, each with a scalar `+` or `-` functional equation.

Thus retaining the pair `(d,F_Nd)` only after PC-311's scalar periodic compression does not recover a new source-native geometric mechanism. It is the classical finite-Fourier/Hurwitz duality available for every even periodic sequence. A surviving Prime-Circle route must add source-forced structure **before** that compression, or introduce a genuinely source-dependent operation on a larger state than the universal Fourier-dual pair.

## 1. Periodic coefficient and normalized finite Fourier transform

Let `N>=2`, and let

\[
d:\mathbb Z/N\mathbb Z\to\mathbb C
\]

be even:

\[
d(-a)=d(a).
\tag{1}
\]

Define the normalized finite Fourier transform

\[
\widehat d(m)
:=(\mathcal F_Nd)(m)
:=\frac1{\sqrt N}\sum_{a\bmod N}d(a)e^{-2\pi iam/N}.
\tag{2}
\]

Evenness is preserved by `F_N`, and the normalized transform satisfies

\[
\mathcal F_N^2d(a)=d(-a)=d(a).
\tag{3}
\]

Hence on the even subspace

\[
\boxed{\mathcal F_N^2=I.}
\tag{4}
\]

For `Re(s)>1`, attach the periodic Dirichlet series

\[
D_d(s):=\sum_{n\ge1}\frac{d(n)}{n^s}.
\tag{5}
\]

Its standard Hurwitz decomposition is

\[
D_d(s)
=N^{-s}\sum_{a=1}^{N}d(a)\,\zeta\!\left(s,\frac aN\right),
\tag{6}
\]

so it has the classical meromorphic continuation of a periodic-coefficient Dirichlet series.

## 2. Hurwitz transformation exchanges `d` and `F_N d`

Use the classical Hurwitz functional transformation in exponential form. After substituting `a/N`, multiplying by `d(a)`, and summing over `a mod N`, the odd sine sector cancels because of (1). The remaining cosine sum is exactly the normalized finite Fourier coefficient:

\[
\sum_{a\bmod N}d(a)\cos\frac{2\pi am}{N}
=\sqrt N\,\widehat d(m).
\tag{7}
\]

Therefore, initially in a common half-plane and then by meromorphic continuation,

\[
\boxed{
D_d(1-s)
=2N^{s-1/2}(2\pi)^{-s}\Gamma(s)
\cos\!\left(\frac{\pi s}{2}\right)
D_{\widehat d}(s).
}
\tag{8}
\]

Introduce the even completion

\[
\Lambda_d(s)
:=\left(\frac N\pi\right)^{s/2}
\Gamma\!\left(\frac s2\right)D_d(s).
\tag{9}
\]

Multiplying (8) by the completion factor at `1-s` and using

\[
\Gamma(s)
=2^{s-1}\pi^{-1/2}
\Gamma\!\left(\frac s2\right)
\Gamma\!\left(\frac{s+1}{2}\right)
\tag{10}
\]

and

\[
\Gamma\!\left(\frac{1-s}{2}\right)
\Gamma\!\left(\frac{1+s}{2}\right)
=\frac{\pi}{\cos(\pi s/2)},
\tag{11}
\]

gives the exact identity

\[
\boxed{
\Lambda_d(1-s)=\Lambda_{\widehat d}(s).
}
\tag{12}
\]

Applying (12) once more and using (4) yields

\[
\boxed{
\Lambda_{\widehat d}(1-s)=\Lambda_d(s).
}
\tag{13}
\]

No arithmetic property of `d` has entered beyond even periodicity.

## 3. The vector functional equation is the universal swap representation

Set

\[
V_d(s)
:=
\begin{pmatrix}
\Lambda_d(s)\\
\Lambda_{\widehat d}(s)
\end{pmatrix}.
\tag{14}
\]

Equations (12)--(13) are exactly

\[
\boxed{
V_d(1-s)=J\,V_d(s),
\qquad
J:=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
}
\tag{15}
\]

The matrix `J` is independent of `N`, of the support of `d`, and of every Prime-Circle source parameter. Diagonalizing it gives the two universal eigensectors

\[
\Lambda_+(s):=\Lambda_d(s)+\Lambda_{\widehat d}(s),
\qquad
\Lambda_-(s):=\Lambda_d(s)-\Lambda_{\widehat d}(s),
\tag{16}
\]

with

\[
\boxed{
\Lambda_+(1-s)=\Lambda_+(s),
\qquad
\Lambda_-(1-s)=-\Lambda_-(s).
}
\tag{17}
\]

Equivalently, the coefficient vectors

\[
d_+:=d+\mathcal F_Nd,
\qquad
d_-:=d-\mathcal F_Nd
\tag{18}
\]

satisfy

\[
\boxed{
\mathcal F_Nd_+=d_+,
\qquad
\mathcal F_Nd_-=-d_-.
}
\tag{19}
\]

So the apparent two-component repair contains no hidden matrix dynamics. It is just the regular two-dimensional representation of the involution `F_N`, and it splits immediately into the two scalar Fourier-eigenvector combinations that PC-312 already identified as possible only by an additional symmetrization step.

## 4. Application to the canonical PC-311/PC-312 packet

For distinct primes `q,r>3`, PC-312's canonical mixed coefficient has `N=qr`, is real and even, and obeys

\[
d(q)=d(r)=0,
\qquad
(\mathcal F_Nd)(q)=(\mathcal F_Nd)(r)=\frac2{\sqrt N}.
\tag{20}
\]

Thus `d` and `F_Nd` are genuinely distinct. PC-312 used exactly this mismatch to prove that `D_d` alone is not scalar self-dual. Equations (12)--(15) now show what happens if both components are retained: closure is automatic, but the closing operator is the universal swap `J` rather than a Prime-Circle-derived mixed-conductor interaction.

There is an additional useful control at the zero residue. PC-312 gives

\[
(\mathcal F_Nd)(0)=\frac2{\sqrt N},
\qquad d(0)=0.
\tag{21}
\]

By finite Fourier inversion,

\[
\sum_{a\bmod N}d(a)=2,
\qquad
\sum_{a\bmod N}(\mathcal F_Nd)(a)=0.
\tag{22}
\]

Hence the periodic series `D_d` has residue `2/N` at `s=1`, whereas `D_{F_Nd}` has zero mean and no corresponding periodic-series pole there. The vector relation therefore does not secretly produce a new xi-like entire object; it exchanges the ordinary meromorphic data required by the universal periodic-series transform. One may of course apply further universal polar clearing or take the eigensector combinations (16), but neither operation is forced by the Prime-Circle source.

The project-specific conclusion is therefore

\[
\boxed{
\text{canonical periodic packet}
\longrightarrow(d,\mathcal F_Nd)
\longrightarrow\text{two-component functional equation}
}
\]

is not a new bridge to the zeta critical line. Once the packet has been reduced to one even periodic coefficient vector, the two-component closure exists for every such vector.

## 5. Prior-art and novelty audit

The transform mechanism is classical; novelty is not claimed for equations (8)--(19).

- Saverio Salerno, Antonio Vitolo and Umberto Zannier, **Functional equations for Dirichlet series with periodic coefficients**, *Ricerche di Matematica* 40 (1991), 209--222, explicitly studies functional relations between Dirichlet series with periodic coefficients and their transforms, with the classical zeta and Dirichlet `L` functional equations as special cases. This is the closest prior-art anchor for the vector transform used here.
- Makoto Ishibashi and Shigeru Kanemitsu, **Dirichlet series with periodic coefficients**, *Results in Mathematics* 35 (1999), 70--88, DOI `10.1007/BF03322023`, treats periodic arithmetic functions and their Dirichlet series as a general framework containing ordinary characters and Dirichlet `L`-functions.
- Anne-Maria Ernvall-Hytönen, Almasa Odžak and Lejla Smajlović, **On a class of periodic Dirichlet series with functional equation**, *Mathematical Communications* 25:1 (2020), 35--47, gives the finite-Fourier coefficient criterion used by PC-312 to characterize the special scalar self-dual degree-one subclass.

The Mathia-specific contribution is the exact boundary statement obtained by applying this classical transform theory to the live PC-312 escape route: the pair `(d,F_Nd)` does close, but its matrix functional equation is **source-independent** and diagonalizes to the manually symmetrized Fourier eigensectors. Therefore the minimal vector-valued completion does not restore information or geometry lost in the PC-311 periodic scalarization.

This also sharpens the interpretation of PC-312. Failure of scalar self-duality is not repaired in a meaningful Prime-Circle sense merely by doubling the state to include the Fourier dual. The repair is formal and universally available; a substantive mechanism would have to explain why a richer source-native state, coupling, positivity law, spectral operator, or destination theorem is present before the classical periodic-series transform takes over.

## 6. Boundary and surviving mechanisms

This result closes only the minimal post-compression route

\[
D_d
\longrightarrow
(D_d,D_{\mathcal F_Nd})
\longrightarrow
\text{new Prime-Circle vector functional equation}.
\tag{23}
\]

It does **not** rule out:

- a source-forced matrix or nonlinear operation acting on the two prime-level fields before they collapse to the single periodic coefficient `d`;
- a larger state retaining independent Fourier indices, vertex data, radial depths, or non-circulant pointed/shell-dependent information not reconstructible from `(d,F_Nd)`;
- an intrinsic source-dependent coupling whose functional-equation matrix is not conjugate to the universal finite-Fourier involution;
- a separately proved zero-sensitive destination theorem that uses additional geometric positivity or spectral information rather than functional-equation symmetry alone.

Those mechanisms change the information carrier. Merely retaining the Fourier transform of the already-compressed packet does not.

## 7. Falsification hooks

This finding should be revised or withdrawn if any of the following occurs:

1. the PC-312 coefficient `d` is not even or is not genuinely `N`-periodic under the conventions of PC-311;
2. the normalized transform convention in (2) is incompatible with PC-312's `F_N`, so that `F_N^2` is not reflection and (4) fails on the canonical packet;
3. the Hurwitz transformation yields an additional source-dependent term after summing an even periodic coefficient, invalidating (8) or the completion (12);
4. the gamma-factor simplification (10)--(11) does not give the exact exchange `Lambda_d(1-s)=Lambda_{F_Nd}(s)`;
5. an independently forced Prime-Circle operation is proved to couple information not determined by `(d,F_Nd)` before periodic scalarization, in which case the present negative remains valid only for the minimal post-compression Fourier-pair repair.

Absent such a failure, the vector-valued functional-equation escape explicitly left open by PC-312 is classical at the minimal two-component level: it is universal Hurwitz/finite-Fourier duality, not a new Prime-Circle mechanism.