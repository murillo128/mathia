# PC-421 — continuous-scale Hilbert commutator is compact Mellin repackaging, not a zero selector

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-HANKEL/COMMUTATOR` + `DECISIVE-NEGATIVE` for the most scale-free continuous-translation/Hilbert-transform compact repair naturally suggested by PC-420. The construction genuinely escapes the no-compact theorem of PC-420 and produces a nonzero Hilbert--Schmidt operator from the exact cyclotomic radial flux. However, it does so for **every** vertical Mellin line `Re(s)=sigma>0`, not specifically for `1/2`; on `0<sigma<1` its symbol Fourier zeros are exactly the already-known zeta zeros lying on that chosen vertical line; and its compact spectrum is invariant under dilations that rescale those Fourier-zero ordinates. Thus the compact operator is a standard Hankel repackaging of the classical PC-179 Mellin data, not a Hilbert--Polya selector or a mechanism forcing the critical line.

This closes only the canonical continuous-scale Hilbert-commutator branch. It does not exclude a source-forced operator that couples different `sigma` values, derives an intrinsic `sigma <-> 1-sigma` relation, mixes angular/old-new data with scale before Mellinization, or introduces a genuinely different nonlocal kernel whose spectral parameter is not merely the Fourier variable of log radius.

## 1. Exact cyclotomic half-density family

PC-179 starts from the source-native radial flux

\[
\rho_n(x)
=-\frac{d}{dx}\log\Phi_n(e^{-x})
=-\sum_{k\ge1}c_n(k)e^{-kx},
\qquad x>0,
\tag{1}
\]

with Mellin transform

\[
\mathcal R_n(s)
:=\int_0^\infty \rho_n(x)x^{s-1}\,dx
=-\Gamma(s)\zeta(s)n^{1-s}
\prod_{p\mid n}(1-p^{s-1}),
\qquad \Re s>0.
\tag{2}
\]

For `sigma>0`, put log radius `u=log x` and define

\[
\boxed{
h_{n,\sigma}(u):=e^{\sigma u}\rho_n(e^u).
}
\tag{3}
\]

Because `rho_n(x)=phi(n)/2+O(x)` as `x->0+` and decays exponentially in `x` as `x->infinity`, both `h_{n,sigma}` and its first derivative decay exponentially as `u->-infinity` and super-exponentially as `u->+infinity`. In particular

\[
h_{n,\sigma}\in H^1(\mathbb R)\cap C_0(\mathbb R)
\qquad(\sigma>0).
\tag{4}
\]

With the unitary Fourier convention

\[
\widehat f(t)
=(2\pi)^{-1/2}\int_{\mathbb R}e^{-itu}f(u)\,du,
\tag{5}
\]

the change of variables `x=e^u` gives the exact Mellin--Fourier identity

\[
\boxed{
\widehat h_{n,\sigma}(t)
=(2\pi)^{-1/2}\mathcal R_n(\sigma-it).
}
\tag{6}
\]

Thus for `0<sigma<1`, where every finite Euler factor in (2) is nonzero,

\[
\boxed{
\widehat h_{n,\sigma}(t)=0
\iff
\zeta(\sigma-it)=0.
}
\tag{7}
\]

This is not a new zeta representation: it is exactly PC-179 written in the unitary log-radius coordinate. It is important nevertheless because it lets us test the continuous-scale compactness loophole of PC-420 without inserting zeta by hand.

At `sigma=1/2`, (3) is the ordinary radial `L^2(dx)` half-density:

\[
\|h_{n,1/2}\|_{L^2(du)}^2
=\int_0^\infty |\rho_n(x)|^2\,dx.
\tag{8}
\]

More generally

\[
\|h_{n,\sigma}\|_{L^2(du)}^2
=\int_0^\infty |\rho_n(x)|^2x^{2\sigma-1}\,dx.
\tag{9}
\]

So `1/2` is distinguished here only by choosing unweighted radial Lebesgue measure. The same source supports the whole weighted vertical-line family.

## 2. The scale generator supplies a canonical nonlocal commutator

Let `H` be the real-line Hilbert transform on `L^2(R)`, normalized by

\[
(Hf)(u)=\frac1\pi\,\operatorname{p.v.}
\int_{\mathbb R}\frac{f(v)}{u-v}\,dv,
\tag{10}
\]

so under (5) it has multiplier `-i sgn(t)`. Equivalently, if `P=-i d/du` is the self-adjoint generator of continuous log-scale translations, `H=-i sgn(P)`. This is the scale-free orientation operator attached to the continuous translation group singled out as a surviving boundary in PC-420; no length scale or zeta parameter is inserted.

For the source symbol (3), define

\[
\boxed{
C_{n,\sigma}:=[H,M_{h_{n,\sigma}}].
}
\tag{11}
\]

Since `H*=-H` and `M_h*=M_h` for real `h`, the commutator is self-adjoint. Its integral kernel is

\[
\boxed{
K_{n,\sigma}(u,v)
=\frac{h_{n,\sigma}(v)-h_{n,\sigma}(u)}
{\pi(u-v)}.
}
\tag{12}
\]

This is genuinely non-diagonal in log scale. It is precisely the kind of continuous integrated coupling excluded from the finite-shift norm algebra of PC-420.

In Fourier variables,

\[
\widehat{C_{n,\sigma}}(\xi,\eta)
=-\frac{i}{\sqrt{2\pi}}
\bigl(\operatorname{sgn}\xi-\operatorname{sgn}\eta\bigr)
\widehat h_{n,\sigma}(\xi-\eta).
\tag{13}
\]

Hence

\[
\begin{aligned}
\|C_{n,\sigma}\|_{\mathcal S_2}^2
&=\frac{2}{\pi}
\int_{\mathbb R}|t|\,|\widehat h_{n,\sigma}(t)|^2\,dt\\
&=\boxed{
\frac1{\pi^2}
\int_{\mathbb R}|t|\,
|\mathcal R_n(\sigma-it)|^2\,dt
}.
\end{aligned}
\tag{14}
\]

The integral is finite by (4), so `C_{n,sigma}` is Hilbert--Schmidt and therefore compact. PC-420's compactness obstruction is thus genuinely escaped once the individual rational-log shifts are replaced by a continuous scale singular integral.

Substituting (2) into (14) gives the exact source specialization

\[
\boxed{
\|C_{n,\sigma}\|_{\mathcal S_2}^2
=
\frac{n^{2(1-\sigma)}}{\pi^2}
\int_{\mathbb R}|t|
|\Gamma(\sigma-it)\zeta(\sigma-it)|^2
\prod_{p\mid n}|1-p^{\sigma-1-it}|^2\,dt.
}
\tag{15}
\]

On the half-density line, `|Gamma(1/2+it)|^2=pi/cosh(pi t)`, so

\[
\boxed{
\|C_{n,1/2}\|_{\mathcal S_2}^2
=
\frac n\pi
\int_{\mathbb R}
\frac{|t|}{\cosh(\pi t)}
|\zeta(1/2+it)|^2
\prod_{p\mid n}|1-p^{-1/2-it}|^2\,dt.
}
\tag{16}
\]

Equation (16) looks RH-adjacent, but it is only a positive weighted second moment of the already-classical Mellin transform. Individual zeros have measure zero and are not selected by this scalar spectral invariant.

## 3. The operator is exactly a classical Hankel block

Let

\[
P_+=\frac{I+iH}{2},
\qquad
P_-=\frac{I-iH}{2}
\tag{17}
\]

be the positive- and negative-frequency Hardy projections. Put

\[
A_{n,\sigma}:=P_-M_{h_{n,\sigma}}P_+.
\tag{18}
\]

Relative to `P_+L^2 \oplus P_-L^2`, equation (11) is

\[
\boxed{
C_{n,\sigma}
=\begin{pmatrix}
0&-2iA_{n,\sigma}^*\\
2iA_{n,\sigma}&0
\end{pmatrix}.
}
\tag{19}
\]

Thus the nonzero eigenvalues of the compact self-adjoint operator are

\[
\boxed{
\lambda_j(C_{n,\sigma})=\pm 2s_j(A_{n,\sigma}),
}
\tag{20}
\]

where `s_j` are the singular values of a standard Hardy/Hankel operator. Equivalently, `C_{n,sigma}` anticommutes with `H`, so its compact spectrum is automatically symmetric about zero.

Nothing zeta-specific is responsible for compactness, the `+/-` pairing, or the Schatten classification. Those are generic properties of Hilbert-transform commutators with sufficiently regular symbols. The Prime-Circle source only chooses the particular symbol `h_{n,sigma}`.

The map from a decaying symbol to the full commutator is essentially lossless rather than magically spectralizing it: from (12), `C_h=0` forces `h(u)=h(v)` for almost every pair, hence `h` is constant; inside `C_0(R)` that constant is zero. Therefore any zeta information recoverable from the **full kernel** is simply information already present in `h` and hence in the classical Mellin transform (6).

## 4. Two exact controls rule out a critical-line spectral interpretation

### 4.1 Every vertical line gives the same compact architecture

For each `sigma>0`, the same construction (3), (11) is Hilbert--Schmidt. In the critical strip, (7) says its symbol Fourier zeros are exactly the zeta zeros lying on the chosen vertical line. There is no operator-theoretic transition at `sigma=1/2`:

\[
\boxed{
0<\sigma<1
\quad\Longrightarrow\quad
C_{n,\sigma}\in\mathcal S_2.
}
\tag{21}
\]

Thus choosing `sigma=1/2` first and observing critical-line zeta zeros in the symbol cannot prove that all nontrivial zeros lie there. If RH were false, the same construction at the offending real part `sigma` would encode those off-line zeros just as well. The half-density exponent is a Hilbert-space measure choice, not a zero-selection theorem.

The smallest shell already makes the classicality explicit. PC-179 gives

\[
\mathcal R_2(s)=\Gamma(s)\eta(s)
=\Gamma(s)(1-2^{1-s})\zeta(s).
\tag{22}
\]

Therefore the shell-2 commutator has exactly the same strip-zero locations in its Mellin/Fourier symbol as every other shell, up to a nonvanishing elementary factor. No collective prime-shell interaction is needed to manufacture (7).

### 4.2 Compact spectral data cannot determine the Fourier-zero ordinates

There is a stronger purely operator-theoretic obstruction. For `c>0`, let

\[
(D_cf)(u)=c^{1/2}f(cu).
\tag{23}
\]

The Hilbert transform is dilation invariant,

\[
D_cHD_c^*=H,
\tag{24}
\]

and

\[
D_cM_hD_c^*=M_{h(c\,\cdot)}.
\tag{25}
\]

Hence for every sufficiently regular real symbol

\[
\boxed{
C_{h(c\,\cdot)}=D_cC_hD_c^*.
}
\tag{26}
\]

The two commutators have **identical compact spectra, singular values, and regularized spectral determinants**. But

\[
\widehat{h(c\,\cdot)}(t)=c^{-1}\widehat h(t/c),
\tag{27}
\]

so every nonzero Fourier zero ordinate is multiplied by `c`.

Consequently no invariant depending only on the compact spectrum of this Hilbert-commutator architecture can determine the Fourier-zero ordinate scale. The actual Prime-Circle geometry fixes one preferred log-radius coordinate, but then it is the source symbol in that coordinate -- not the unitary spectrum of the commutator -- that carries the zeta ordinates. This decisively separates (7) from a Hilbert--Polya statement.

## 5. Prior-art and novelty audit

The operator theory is classical. Coifman--Rochberg--Weiss, **Factorization theorems for Hardy spaces in several variables**, *Annals of Mathematics* 103 (1976), 611--635, DOI `10.2307/1970954`, established the foundational relation between BMO and commutators with singular integrals. Uchiyama, **On the compactness of operators of Hankel type**, *Tohoku Mathematical Journal* 30 (1978), 163--171, DOI `10.2748/tmj/1178230105`, gives the classical compactness boundary. Janson--Wolff, **Schatten classes and commutators of singular integral operators**, *Arkiv for Matematik* 20 (1982), 301--310, DOI `10.1007/BF02390515`, and Peller's subsequent Hankel/Schatten theory (including *Hankel Operators and Their Applications*, Springer, 2003, DOI `10.1007/978-0-387-21681-2`) place formulas such as the `H^{1/2}`/Hilbert--Schmidt criterion squarely in established harmonic/operator analysis. A modern summary is Fan--Lacey--Li, *Journal of Fourier Analysis and Applications* 29 (2023), article 17, DOI `10.1007/s00041-023-09995-1`, which explicitly identifies the Euclidean Peller/Janson--Wolff/Rochberg--Semmes commutator results as the classical antecedents.

No historical novelty is claimed for Hilbert transforms, Hardy projections, Hankel operators, Schatten criteria, Mellin--Plancherel coordinates, or dilation covariance. The project-specific contribution is the exact insertion of the Prime-Circle radial flux into this continuous-scale compact architecture and the resulting classification: equations (6), (14)--(16), the all-vertical-lines control (21), and the spectral-dilation obstruction (26)--(27) show exactly why this natural escape from PC-420 does not become an RH zero selector.

The novelty audit also checks against the line's earlier internal boundaries. PC-075 already showed that an angular Hardy coupling of the cyclotomic boundary logarithm reduces to universal Hilbert channels; PC-179 showed that one-shell radial Mellinization already contains zeta classically; PC-374 showed that a natural appearance of `1/2` can be a universal half-density gauge; and PC-420 left continuous integrated/resolvent scale operators open because they can contain compact ideals. PC-421 sits precisely at the intersection of those four facts rather than duplicating any one of them.

## 6. Falsification and surviving frontier

The exact claims can be checked independently at the following load-bearing points: the change of variables in (6); the Hilbert-commutator Fourier kernel (13); the measure of opposite-sign frequency pairs giving the constant `2/pi` in (14); the PC-179 factorization inserted into (15); the Hardy block decomposition (19); and the unitary dilation covariance (26). Failure of any of these would invalidate the classification.

The result does **not** say that every continuous-scale or compact source operator is spectrally useless. It rules out the specific scale-free Hilbert-transform commutator, and more conceptually it shows that merely turning the classical Mellin symbol into a compact Hankel operator does not create a critical-line theorem. A surviving mechanism must add a relation absent here, such as a source-forced coupling between `sigma` and `1-sigma`, a cross-shell operator whose spectrum is not invariant under arbitrary log-frequency rescaling, or a genuinely two-dimensional/angular-old-new interaction that is formed before the one-shell Mellin transform.

In particular, a future compact repair should be tested immediately against two controls exposed here: **does the same construction exist for every vertical Mellin weight, and can a unitary reparameterization move the candidate zero ordinates without changing the operator spectrum?** If either answer is yes, the construction has not yet supplied the missing RH mechanism.