# WI-366 — Desogus's true gamma image cannot uniformly dominate the bare Carleman channel

**Status:** `EXACT-DERIVED + PRIMARY-SOURCE-CRITICAL-AUDIT + DECISIVE-REPAIR-BARRIER + NON-ESTABLISHED-RH`.

## Claim

The exact positive gamma-image channel isolated in WI-365,

\[
(J_Af)(u)=\int_0^1 j_A(u,v)f(v)\,dv,
\qquad
j_A(u,v)=A\frac{e^{-A(u+v)/2}}{1-e^{-2A(u+v)}},
\tag{1}
\]

cannot supply the fixed bare-Carleman OSPR reserve of Marco Desogus's 17 September 2026 preprint by any uniform positive Loewner comparison. More precisely, if

\[
(Kf)(u)=\int_0^1\frac{f(v)}{u+v}\,dv,
\tag{2}
\]

then there do not exist constants `c>0` and `A_0` such that

\[
\boxed{J_A\succeq cK\qquad\text{for every }A\ge A_0.}
\tag{3}
\]

In fact, testing on any fixed nonzero nonnegative function supported away from `u=0` forces every possible comparison coefficient `c_A` in `J_A\succeq c_AK` to satisfy

\[
\boxed{c_A=O(Ae^{-A\delta})}
\tag{4}
\]

for some fixed `\delta>0`. The true gamma image becomes a boundary-layer Hankel channel on the normalized cell, whereas the bare Carleman operator remains scale invariant.

A second exact diagnostic makes the mismatch explicit on the constant channel:

\[
\boxed{
\langle 1,J_A1\rangle
\sim
\frac{\pi^2/4+2G}{A},
}
\tag{5}
\]

where `G` is Catalan's constant, while

\[
\boxed{\langle1,K1\rangle=2\log2.}
\tag{6}
\]

Thus the simplest repair branch left open by WI-365 — compare the exact positive image uniformly from below by a fixed copy of the normalized bare Carleman operator and inherit the printed fixed OSPR constant `d_*` — is impossible along the cofinal large-`A` regime used by the rooted induction.

This is a barrier to that **repair mechanism**, not to the claimed theorem itself. A valid proof could still derive a different exact bare-Carleman contribution, establish an `A`-dependent OSPR reserve adapted to `J_A`, or reorganize the source-to-cell transport so that the downstream induction does not need the fixed reserve in the printed form. WI-363's independent diagonal multiplier `W_A` also remains unresolved.

## 1. Exact dilation identifies the true scaling

Write

\[
h(s)=\frac{e^{-s/2}}{1-e^{-2s}},
\qquad s>0,
\tag{7}
\]

so that `j_A(u,v)=Ah(A(u+v))`. Introduce the unitary dilation

\[
D_A:L^2(0,1)\longrightarrow L^2(0,A),
\qquad
(D_Af)(x)=A^{-1/2}f(x/A).
\tag{8}
\]

A direct change of variables gives

\[
\boxed{
D_AJ_AD_A^*=H_A,
\qquad
(H_Ag)(x)=\int_0^A h(x+y)g(y)\,dy.
}
\tag{9}
\]

Thus increasing `A` does not produce a larger multiple of a fixed cell operator. It expands the domain on which the **fixed** Hankel kernel `h(x+y)` is compressed.

For the bare Carleman operator the same dilation gives

\[
\boxed{
D_AKD_A^*=C_A,
\qquad
(C_Ag)(x)=\int_0^A\frac{g(y)}{x+y}\,dy.
}
\tag{10}
\]

The distinction is structural. `1/(x+y)` is homogeneous of degree `-1`, so the normalized bare Carleman channel is dilation invariant. By contrast,

\[
h(s)\sim \frac1{2s}\quad(s\downarrow0),
\qquad
h(s)\sim e^{-s/2}\quad(s\to\infty),
\tag{11}
\]

so the exact gamma image retains the local singularity only near the endpoint and decays exponentially away from it.

## 2. No uniform Loewner transfer from the true image to bare Carleman

Fix `\delta\in(0,1)` and a nonzero nonnegative `f\in L^2(0,1)` supported in `[\delta,1]`. For `u,v` in this support, `u+v\ge2\delta`, hence from (1)

\[
0\le j_A(u,v)
\le
\frac{Ae^{-A\delta}}{1-e^{-4A\delta}}.
\tag{12}
\]

Therefore

\[
0\le
\langle f,J_Af\rangle
\le
\frac{Ae^{-A\delta}}{1-e^{-4A\delta}}\,\|f\|_1^2
\longrightarrow0.
\tag{13}
\]

On the other hand the Carleman kernel is strictly positive on the same support, so

\[
\langle f,Kf\rangle
=
\int_0^1\!\int_0^1
\frac{f(u)f(v)}{u+v}\,du\,dv
>0.
\tag{14}
\]

If (3) held, (13)--(14) would imply

\[
c\,\langle f,Kf\rangle
\le
\langle f,J_Af\rangle
\to0,
\tag{15}
\]

which is impossible. More generally, any coefficient `c_A\ge0` satisfying `J_A\succeq c_AK` obeys the explicit test-vector bound

\[
0\le c_A
\le
\frac{\|f\|_1^2}{\langle f,Kf\rangle}
\frac{Ae^{-A\delta}}{1-e^{-4A\delta}},
\tag{16}
\]

which proves (4).

The argument requires no spectral approximation, numerical quadrature, or conjectural information. It is an exact form comparison on a fixed admissible test vector. It also shows why positivity alone, established in WI-365, is insufficient to transport a fixed quantitative reserve: positivity controls the sign of the omitted channel but not its strength relative to `K`.

## 3. Constant-channel mass also collapses at rate `1/A`

Set

\[
\alpha_A:=\langle1,J_A1\rangle.
\tag{17}
\]

Using (9) with `D_A1=A^{-1/2}` gives

\[
A\alpha_A
=
\int_0^A\!\int_0^A h(x+y)\,dx\,dy.
\tag{18}
\]

Because `h\ge0`, monotone convergence on the expanding square yields

\[
\lim_{A\to\infty}A\alpha_A
=
\int_0^\infty\!\int_0^\infty h(x+y)\,dx\,dy
=
\int_0^\infty s h(s)\,ds.
\tag{19}
\]

The geometric expansion

\[
h(s)=\sum_{m\ge0}e^{-(2m+1/2)s}
\tag{20}
\]

has nonnegative terms, so Tonelli gives

\[
\int_0^\infty s h(s)\,ds
=
\sum_{m\ge0}\frac1{(2m+1/2)^2}
=4\sum_{m\ge0}\frac1{(4m+1)^2}.
\tag{21}
\]

Using the standard decomposition of the odd reciprocal-square series into residue classes modulo four,

\[
\sum_{m\ge0}\frac1{(4m+1)^2}
=\frac{\pi^2}{16}+\frac G2,
\tag{22}
\]

and hence

\[
\lim_{A\to\infty}A\alpha_A
=\frac{\pi^2}{4}+2G,
\tag{23}
\]

which is (5). In contrast,

\[
\langle1,K1\rangle
=
\int_0^1\!\int_0^1\frac{du\,dv}{u+v}
=2\log2,
\tag{24}
\]

independently of `A`.

Equation (23) is not needed for the no-go proof in Section 2; it is an independent exact scaling check. It shows that even the lowest scalar channel of `J_A` does not carry an `A`-independent fraction of the corresponding bare-Carleman mass.

## 4. Consequence for the printed OSPR reserve

Section 4 of `arXiv:2609.20367v1` computes the OSPR rebound using the normalized bare Carleman operator (2), including the fixed constant

\[
d_*=0.4934219\ldots.
\tag{25}
\]

WI-365 established that the true odd-fold gamma image is positive and can therefore be discarded when proving a lower form bound. It left three repair possibilities for the quantitative reserve: exhibit a separate exact `K` channel, compare `J_A` from below with the required normalized `K`, or redo the OSPR estimate for the true `A`-dependent channel.

The present result closes the second possibility **in its uniform fixed-coefficient form**. Since the rooted construction requires a cofinal family of collars with unbounded `A`, (3) cannot provide the fixed lower reserve booked from the bare Carleman operator. Equation (16) is stronger: any whole-operator comparison coefficient extracted this way must collapse at least exponentially on test vectors supported away from the folded endpoint.

The geometry is therefore boundary-layer rather than scale-invariant. For every fixed `\delta>0`, the kernel of `J_A` converges exponentially to zero on `[\delta,1]^2`, while the normalized Carleman kernel remains `1/(u+v)`. Any successful OSPR repair must exploit the actual endpoint concentration and the associated source profile, rather than globally substituting the printed bare-Carleman rebound.

This does not show that an `A`-dependent OSPR quotient for `J_A` vanishes, because such a quotient can involve vectors or affine directions that themselves concentrate near the endpoint as `A` grows. The finding deliberately does not replace that source-aware variational problem by an unsupported scalar inference.

## 5. Interaction with the diagonal transport defect

WI-363 derived the nonconstant multiplier generated by the half-density transport of the singular Cauchy difference form. The exact gamma image and that diagonal correction have different scaling and operator type. The no-comparison theorem above therefore does not repair or worsen `W_A`; it only removes a tempting route for rescuing the quantitative Carleman reserve after safely dropping the positive image.

Consequently the source-to-cell audit now has two sharply separated unresolved tasks. First, the complete diagonal/scalar transport must be reconstructed so that the surviving multiplier is controlled on the common form domain. Second, if the later induction needs a fixed quantitative rebound, its provenance must come from an exact surviving channel or from a new source-aware `A`-dependent estimate. Treating `J_A` as if it were a scale-invariant copy of `K` is no longer an available bridge.

## 6. Prior-art and novelty audit

Primary source: Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, `arXiv:2609.20367v1`, submitted 17 September 2026, especially the normalized bare-Carleman/OSPR calculation in Section 4 and the localized odd source-to-cell transport in Section 5. The source is already anchored in `research/weil_inertia/SOURCES.md`.

A fresh targeted audit on 20 September 2026 found the primary submission and generic listings/mirrors but no independent correction, erratum, or technical discussion resolving the gamma-image normalization and reserve-transfer issue. General dilation properties of Carleman and Hankel operators are classical operator theory; equations (8)--(10) are elementary changes of variables and are not claimed as new general theory. The reciprocal-square identity (22) is also classical.

Mathia's durable contribution here is source-specific and narrower: combining the exact image kernel forced by the preprint's own odd fold with its cofinal large-`A` regime gives a rigorous no-go theorem for the most direct reserve-repair branch left open by WI-365. No claim of literature priority is made.

## 7. Falsification and scope boundaries

The barrier depends on the exact gamma-image kernel (1), derived and sign-checked in WI-364--WI-365. If that kernel or normalization is corrected, equations (9), (13), and (23) should be rerun from the corrected source formula.

This finding would not block a repair that:

- identifies a separate physical channel exactly equal to the normalized bare `K` with the required coefficient;
- proves an `A`-dependent OSPR inequality for `J_A` whose source-aligned reserve remains sufficient for the induction; or
- reorganizes the local coercivity argument so the printed `d_*` is unnecessary.

It does **not** assert that Desogus's main theorem is false, that `J_A` has no useful quantitative coercivity, that its norm tends to zero, or that every possible comparison with Carleman fails. The precise statement is that no `A`-independent positive whole-operator coefficient can satisfy `J_A\succeq cK` along the required cofinal regime, and any coefficient certified by a fixed interior test vector decays as in (16).

## Consequence for the research line

WI-365 left comparison with the bare Carleman block as one of the shortest possible repairs of the claimed source-exact RH mechanism. WI-366 closes that route in the form needed to inherit a fixed OSPR reserve. The next useful audit should therefore avoid further global `J_A\succeq cK` optimization and instead test one of the two remaining source-exact possibilities: reconstruct a genuine additional Carleman channel from the full transport, or derive the OSPR/source-alignment estimate directly for the boundary-layer kernel `J_A` together with the exact diagonal terms. Until one of those bridges is proved, the preprint's cofinal RH conclusion remains outside Mathia's established evidence base.