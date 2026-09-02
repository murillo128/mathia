# WP-119 — Gamma–Schoenberg reflection parity sectors each retain coherent prime divergence

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + GRADED-GRAM + PRIME-CIRCLE-BRIDGE + SHARP-THRESHOLD + MATCHED-CONTROL + PRIOR-ART-AUDITED` for the canonical reflection/parity escape left open by `WP-118`.

`WP-118` proves that the exact one-prime Weil amplitudes cannot be coherently glued through the shared positive Gamma–Schoenberg Hilbert space: on positive prime frequencies its Gram cone is acute, and the shared vector diverges for every deformation exponent `sigma <= 1`. That result explicitly leaves a graded or matrix coupling as a possible escape. The first canonical grading is already present: the symmetric Gamma Lévy measure is invariant under reflection of its jump coordinate, so the Schoenberg space splits orthogonally into even and odd sectors.

That split does **not** create destructive prime interference. For the Prime-Circle-selected real Gamma channel, the even and odd projected Schoenberg kernels are both strictly positive on every pair of positive frequencies. More strongly, on a dyadic prime shell both kernels grow uniformly like a positive multiple of `log log X`. Therefore the coherent prime vector in **either parity sector separately** diverges for every `0 < sigma <= 1`, while each sector converges for `sigma > 1`. The sharp coherent threshold from `WP-118` survives projection to either canonical reflection parity.

This closes the simplest intrinsic graded repair of the Gamma shared-coupling obstruction. It does not exclude a frequency-dependent matrix coupling, a non-reflection-equivariant intertwiner, a quotient/compression formed before the Schoenberg norm, or a genuinely new finite–archimedean cohomological architecture. A signed supertrace can of course subtract the two parity energies, but then the independent positive theorem has been discarded rather than explained.

## 1. The exact Gamma channel has a canonical reflection grading

From `WP-117`, write the Riemann archimedean variation on the critical line as

\[
H_\infty(t)
:=
\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)
-
\psi\!\left(\frac14\right).
\tag{1}
\]

It has the symmetric Lévy representation

\[
H_\infty(t)
=
\int_{\mathbb R}(1-\cos ty)\,\nu_\infty(dy),
\tag{2}
\]

with the exact positive symmetric measure fixed in `WP-117`. Let

\[
\mathcal H_\infty=L^2(\mathbb R,\nu_\infty),
\qquad
\Phi(t)(y)=e^{ity}-1.
\tag{3}
\]

Then

\[
\|\Phi(t)\|^2=2H_\infty(t)
\tag{4}
\]

and the full real Gram kernel is

\[
K(s,t)
=
\langle\Phi(s),\Phi(t)\rangle
=
H_\infty(s)+H_\infty(t)-H_\infty(s-t).
\tag{5}
\]

Because `nu_infty` is symmetric, reflection of the Lévy coordinate defines a canonical unitary involution

\[
(Jf)(y):=f(-y),
\qquad J^2=I.
\tag{6}
\]

Its orthogonal projections are

\[
P_\pm=\frac{I\pm J}{2}.
\tag{7}
\]

Applied to the Schoenberg increment,

\[
\boxed{
\Phi_+(t):=P_+\Phi(t)=\cos(ty)-1,
\qquad
\Phi_-(t):=P_-\Phi(t)=i\sin(ty).
}
\tag{8}
\]

Thus the shared Gamma Hilbert geometry itself supplies the first non-arbitrary `Z_2` grading to test after `WP-118`. This is the archimedean cosine/sine grading induced by the real reflection symmetry; it should not be confused with the primitive-shell cycle grading studied in `WP-049` and `WP-050`.

The relation to Prime Circle is nevertheless canonical at the level needed here. `WP-048` independently selects the order-two real Gamma channel from anchored reflection/cycle extremality, and `WP-117` then realizes that selected Gamma variation as the symmetric Schoenberg energy (1)--(4). No zero data or fitted kernel is used to choose either the channel or the parity split.

## 2. Both parity Gram kernels are exact and strictly positive on positive frequencies

Orthogonality of the parity sectors gives

\[
K=K_++K_-,
\qquad
K_\pm(s,t):=\langle\Phi_\pm(s),\Phi_\pm(t)\rangle.
\tag{9}
\]

For the odd sector, the product-to-sum identity and (2) give

\[
\begin{aligned}
K_-(s,t)
&=
\int_{\mathbb R}\sin(sy)\sin(ty)\,\nu_\infty(dy)\\
&=
\boxed{
\frac12\bigl[
H_\infty(s+t)-H_\infty(|s-t|)
\bigr].
}
\end{aligned}
\tag{10}
\]

For the even sector,

\[
\begin{aligned}
K_+(s,t)
&=
\int_{\mathbb R}(1-\cos sy)(1-\cos ty)\,\nu_\infty(dy)\\
&=
\boxed{
H_\infty(s)+H_\infty(t)
-\frac12H_\infty(s+t)
-\frac12H_\infty(|s-t|).
}
\end{aligned}
\tag{11}
\]

Equation (11) is already nonnegative from its pointwise integral. For the odd sector one needs a property special to the Gamma symbol rather than generic conditional negative definiteness. `WP-118` records the classical digamma series: for `a>0`,

\[
h_a(u)
:=
\operatorname{Re}\psi(a+iu)-\psi(a)
=
\sum_{n=0}^{\infty}
\frac{u^2}{(n+a)((n+a)^2+u^2)}.
\tag{12}
\]

Every summand is strictly increasing for `u>0`, hence `h_a(u)` is strictly increasing there. Since

\[
H_\infty(t)=h_{1/4}(t/2),
\tag{13}
\]

`H_infty` is strictly increasing on positive frequency. Therefore, for `s,t>0`,

\[
s+t>|s-t|
\]

and (10) yields

\[
\boxed{K_-(s,t)>0.}
\tag{14}
\]

The positive density of `nu_infty` also makes the integral in (11) strictly positive for nonzero `s,t`, so

\[
\boxed{K_+(s,t)>0\qquad(s,t>0).}
\tag{15}
\]

Thus reflection does not split the acute Gamma cone into one constructive and one cancelling sector. **Each sector is itself acute on the positive logarithmic frequencies occupied by primes.**

As a consistency check, adding (10) and (11) recovers exactly (5).

## 3. Dyadic prime shells force quantitative divergence in each parity sector

The classical digamma asymptotic gives

\[
H_\infty(u)=\log u+O(1)
\qquad(u\to\infty).
\tag{16}
\]

Fix a large `X` and the dyadic prime shell

\[
\mathcal P_X:=\{p:X<p\le2X\},
\qquad L:=\log X.
\tag{17}
\]

For `p,q in P_X`, put

\[
s=\log p,
\qquad t=\log q.
\]

Then

\[
L\le s,t\le L+\log2,
\qquad
|s-t|\le\log2,
\qquad
s+t\ge2L.
\tag{18}
\]

Monotonicity in (10) therefore gives the uniform odd-sector bound

\[
\begin{aligned}
K_-(s,t)
&\ge
\frac12\bigl[H_\infty(2L)-H_\infty(\log2)\bigr]\\
&=
\boxed{\frac12\log L+O(1).}
\end{aligned}
\tag{19}
\]

For the even sector, use (11), monotonicity, and (18):

\[
\begin{aligned}
K_+(s,t)
&\ge
2H_\infty(L)
-\frac12H_\infty(2L+2\log2)
-\frac12H_\infty(\log2)\\
&=
\boxed{\frac32\log L+O(1).}
\end{aligned}
\tag{20}
\]

Hence there exist `X_0` and constants `c_+,c_->0` such that for all `X>=X_0` and all `p,q in P_X`,

\[
\boxed{
K_\pm(\log p,\log q)
\ge c_\pm\log\log X.
}
\tag{21}
\]

Now use the same matched deformation as `WP-118`, ignoring the irrelevant common normalization constant,

\[
a_{p,\sigma}:=\frac{\log p}{p^\sigma},
\qquad \sigma>0,
\tag{22}
\]

and define the parity-projected coherent shell vectors

\[
V_{X,\sigma}^{\pm}
:=
\sum_{p\in\mathcal P_X}
a_{p,\sigma}\Phi_\pm(\log p).
\tag{23}
\]

All amplitudes are positive and all parity Gram entries in (21) are positive, so

\[
\boxed{
\|V_{X,\sigma}^{\pm}\|^2
\ge
c_\pm\log\log X
\left(
\sum_{X<p\le2X}\frac{\log p}{p^\sigma}
\right)^2.
}
\tag{24}
\]

By the prime number theorem and partial summation,

\[
\sum_{X<p\le2X}\frac{\log p}{p^\sigma}
\asymp X^{1-\sigma}
\qquad(0<\sigma<1),
\tag{25}
\]

while at the endpoint

\[
\sum_{X<p\le2X}\frac{\log p}{p}
\longrightarrow\log2.
\tag{26}
\]

Equations (24)--(26) imply

\[
\boxed{
\|V_{X,\sigma}^{\pm}\|\longrightarrow\infty
\qquad(0<\sigma\le1).
}
\tag{27}
\]

At `sigma=1`, the lower bound already grows like a positive constant times `log log X` at the energy level.

This shell argument is enough to rule out convergence of the global coherent prime sum. In fact (14)--(15) give a stronger monotonicity: because all pairwise Gram terms are positive, enlarging a finite set of positive prime frequencies can only increase the squared norm. No cancellation between different prime shells can undo (27).

## 4. The matched convergence control remains sigma greater than one

The obstruction has a sharp control. Orthogonal projection cannot increase norm, so from (4)

\[
\|\Phi_\pm(t)\|
\le
\|\Phi(t)\|
=\sqrt{2H_\infty(t)}.
\tag{28}
\]

Using (16),

\[
\|\Phi_\pm(\log p)\|
=O(\sqrt{\log\log p}).
\tag{29}
\]

Therefore, for every `sigma>1`,

\[
\sum_p
\frac{\log p}{p^\sigma}
\|\Phi_\pm(\log p)\|
<\infty,
\tag{30}
\]

because the corresponding integer series with the extra `sqrt(log log n)` factor converges. The parity-projected coherent series consequently converges absolutely in `H_infty`.

Combining (27) and (30), each canonical parity sector has the exact same threshold as the full shared coupling:

\[
\boxed{
\sum_p\frac{\log p}{p^\sigma}\Phi_\pm(\log p)
\text{ converges in }\mathcal H_\infty
\iff
\sigma>1.
}
\tag{31}
\]

Thus the reflection grading does not improve the critical summability even infinitesimally.

## 5. Positive block weighting cannot use parity to cancel the obstruction

A fixed reflection-equivariant positive quadratic form on the two parity channels has the simplest block form

\[
\mathcal E_{c_+,c_-}(P)
=
c_+\|V_P^+\|^2+c_-\|V_P^-\|^2,
\qquad c_+,c_-\ge0.
\tag{32}
\]

If at least one coefficient is nonzero, (27) implies

\[
\boxed{
\sup_{P\Subset\mathcal P}
\mathcal E_{c_+,c_-}(P)=+\infty
\qquad(0<\sigma\le1).
}
\tag{33}
\]

A signed combination such as

\[
\|V_P^+\|^2-\|V_P^-\|^2
\tag{34}
\]

can create cancellation, but it is no longer nonnegative by an independent Hilbert-space theorem. That is exactly the distinction imposed by the research mandate: introducing a grading is useful only if the final Weil-type form inherits positivity from the geometry rather than from a later sign choice or RH-equivalent identity.

Equation (33) is intentionally narrower than a no-go for all graded geometries. Frequency-dependent positive matrix weights, non-diagonal intertwiners between finite and archimedean sectors, quotients/compressions with a new theorem of sign, or non-reflection-equivariant structures are outside its scope.

## 6. Adversarial controls and prior-art audit

Several immediate falsification routes were checked.

First, positivity of the odd kernel was **not** inferred merely from Schoenberg conditional negative definiteness; that would be invalid in general. It follows here from the exact Gamma digamma series (12), which proves strict monotonicity of `H_infty`. Even-sector positivity follows directly from the nonnegative integral in (11).

Second, the conclusion is not a diagonal-energy restatement of `WP-117` or `WP-115`. The vectors are summed coherently inside one shared infinite-dimensional Hilbert space before taking a norm, and the parity projection is performed before that sum. Cross-prime terms are present in both sectors. Equations (19)--(24) show that those cross terms remain quantitatively constructive.

Third, this is not the primitive-shell reflection cancellation of `WP-049` or the odd cycle current of `WP-050`. Those results act on the profinite/cyclotomic character shells of Prime Circle and study finite Mangoldt extraction. Here the involution acts on the Lévy jump coordinate of the exact archimedean Gamma Schoenberg realization. The two constructions meet only through the independently selected real `q=2` channel of `WP-048`.

Fourth, the `sigma>1` control in (30)--(31) shows that the divergence is tied to the arithmetic critical carrier and not to a pathological definition of the parity projections.

The external ingredients used here are classical: the Schoenberg/Lévy Hilbert realization, the digamma series and asymptotic, elementary sine/cosine product identities, and the prime number theorem with partial summation. The bounded prior-art audit surface already recorded in `SOURCES.md` covers these ingredients and the relevant Weil/Connes/Sonin/Hilbert–Pólya comparison classes. Searches for a digamma-Schoenberg reflection-parity prime coupling did not reveal a literature theorem matching the Mathia-specific composition above. The claim of novelty is therefore limited to this exact bridge and obstruction, not to any of the classical component identities.

## 7. Consequence for the Weil-positivity search

The canonical route now has a sharper boundary:

\[
\boxed{
\text{Prime-Circle }q=2\text{ selector}
\longrightarrow
\text{Gamma Schoenberg positivity}
\longrightarrow
\text{reflection parity split}
\longrightarrow
\text{two separately acute prime cones}
\longrightarrow
\text{coherent divergence for }\sigma\le1.
}
\tag{35}
\]

So the first natural graded refinement of the independently positive archimedean geometry does not supply the missing sign-changing cross-prime mechanism. A surviving Mathia-native global Weil form must alter the architecture **before** the final positive norm in a way stronger than constant reflection parity: for example through a geometrically forced frequency-dependent matrix/intertwining structure, a nontrivial quotient or primitive cohomological sector, or a finite–archimedean coupling whose sign theorem is not just positivity of the raw Gamma Schoenberg space.

That remaining requirement is substantive. `WP-118` showed that ungraded coherent Gamma gluing is too positive; the present result shows that its canonical `Z_2` decomposition is still too positive **in each component separately**.
