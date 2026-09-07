# ANF-103 — source-negligible trimming makes superlinear escape a source-heavy-tail problem

**Status:** `EXACT-DERIVED + QUANTITATIVE-TRIMMING-STABILITY + CONCENTRATION-COMPACTNESS-REDUCTION + UNIVERSAL-SPARSE-TAIL-HEIGHT-THRESHOLD + NOTCH-ENVELOPE-NARROWING`. `ANF-099` reduces the fixed central-notch route to the exposure of physical Montgomery--Taylor near-extremizers. `ANF-100` forces every growing near-extremizer to have at least linear horizontal span, while `ANF-101` shows that the vertically weighted empirical bulk is tight whenever that span is at most linear. The remaining list there treats a source-relevant sparse height tail and superlinear horizontal escape as distinct possibilities. They are not independent. A superlinear diameter created by points whose Montgomery--Taylor source norm is negligible can be deleted without changing either near-extremality or the limiting notch exposure. Therefore superlinear escape is a genuinely new chamber only when the escaping tail is **source-heavy**.

The same argument gives a universal quantitative threshold for an ultra-sparse source-heavy tail. Because the Montgomery--Taylor spectrum vanishes linearly at the endpoints of `[-1,1]`, a tail of `m` points below height `H` has source energy at most order

\[
m^2\frac{e^{4\pi H}}{H^2}.
\]

Consequently, if such a tail is to carry a macroscopic fraction of the source norm of a configuration with affine size `L`, and `L/m^2\to\infty`, then necessarily

\[
\boxed{
4\pi H
\ge
\log\frac{L}{m^2}
+2\log\log\frac{L}{m^2}
+O(1).
}
\]

For the `N\asymp n^3`, `m\asymp n` sparse-surgery scale of `ANF-095`, this becomes `4 pi H >= log n + 2 log log n + O(1)`: the matched log--log threshold found there is therefore not an arithmetic accident of that construction, but the universal endpoint cost of making a sub-square-root tail source-visible.

## 1. Exact trimming stability in the Montgomery--Taylor Hilbert norm

Retain the notation of `ANF-099`:

\[
J_0:=J_{\rm MT},
\qquad
S_W(\alpha):=\sum_{z\in W}e^{-2\pi i\alpha z},
\qquad
L(W):=2|W|-\sigma(W),
\]

\[
r(W):=\frac{\|S_W\|_0^2}{L(W)},
\qquad
h_\eta(W):=
\frac{\int\phi_\eta(\alpha)|S_W(\alpha)|^2\,d\alpha}{L(W)},
\]

where `||f||_0^2=int J_0 |f|^2` and `0<=phi_eta<=J_0`.

Let `I` be any real interval and split a finite conjugation-invariant multiset by horizontal center,

\[
A:=\{z\in W:\Re z\in I\},
\qquad
B:=W\setminus A.
\]

Because conjugate points have the same real part, both pieces remain conjugation-invariant. The split also keeps every real support site intact, so the affine bookkeeping is exactly additive:

\[
L(W)=L(A)+L(B).
\]

Put

\[
e:=r(W)-1\ge0,
\qquad
\mu:=\frac{L(B)}{L(W)},
\qquad
\tau:=\frac{\|S_B\|_0}{\sqrt{L(W)}}.
\]

Since `S_A=S_W-S_B`, the triangle inequality gives

\[
\|S_A\|_0
\le
\sqrt{L(W)}\bigl(\sqrt{1+e}+\tau\bigr).
\]

Lamzouri's Montgomery--Taylor inequality applies independently to `A`, so `r(A)>=1`. Combining the two statements yields the finite quantitative estimate

\[
\boxed{
0\le r(A)-1
\le
\frac{\bigl(\sqrt{1+e}+\tau\bigr)^2}{1-\mu}-1.
}
\tag{1}
\]

Thus a source-small deletion cannot destroy near-extremality.

The same is true for the fixed-notch exposure. Let `M_eta` denote multiplication by `sqrt(phi_eta/J_0)` on the support where `J_0>0`; then `||M_eta f||_0<=||f||_0` and

\[
h_\eta(W)=\frac{\|M_\eta S_W\|_0^2}{L(W)}.
\]

Polarization and contraction give

\[
\left|
\|M_\eta S_A\|_0^2-
\|M_\eta S_W\|_0^2
\right|
\le
L(W)\left(2\sqrt{1+e}\,\tau+\tau^2\right).
\]

Since `h_eta(W)<=r(W)=1+e` and `L(A)=(1-mu)L(W)`, one obtains

\[
\boxed{
|h_\eta(A)-h_\eta(W)|
\le
\frac{
2\sqrt{1+e}\,\tau+\tau^2+\mu(1+e)
}{1-\mu}.
}
\tag{2}
\]

No spatial sign of the Montgomery--Taylor transform is used. Equations (1)--(2) are just Hilbert geometry plus the exact affine bookkeeping of a center-complete horizontal trimming.

## 2. Superlinear diameter caused by a negligible tail is not a new escape

Let `W_n` be a growing physical near-extremizer,

\[
N_n:=|W_n|\to\infty,
\qquad
r(W_n)\to1.
\]

Suppose there are horizontal intervals `I_n` and associated decompositions `W_n=A_n\sqcup B_n` as above such that

\[
|B_n|=o(N_n),
\qquad
\frac{\|S_{B_n}\|_0^2}{L(W_n)}\to0.
\tag{3}
\]

Because `N_n<=L(W_n)<=2N_n` and `L(B_n)<=2|B_n|`, equation (3) implies `mu_n->0` and `tau_n->0`. Equations (1)--(2) therefore give

\[
\boxed{
r(A_n)\to1,
\qquad
h_\eta(A_n)-h_\eta(W_n)\to0.
}
\tag{4}
\]

In particular, if `W_n` is a candidate witnessing the dangerous envelope in `ANF-099`, then `A_n` is an equally dangerous candidate asymptotically. A remote tail that is negligible in the actual Montgomery--Taylor source norm cannot be used to manufacture a new fixed-notch obstruction merely by making the raw diameter enormous.

Now assume additionally that the retained interval has only linear length,

\[
|I_n|=O(N_n).
\tag{5}
\]

Since `|A_n|=N_n-o(N_n)`, the retained sequence satisfies `D_x(A_n)=O(|A_n|)`. Hence `ANF-101` applies directly to `A_n`: after horizontal recentering and scaling by `|A_n|`, its empirical vertical mass is exponentially tight. Therefore an apparent `D_x(W_n)/N_n->infinity` caused by deleting a source-negligible `o(N_n)` tail does **not** evade the linear-span chamber. It reduces back to it without changing the limiting exposure.

This merges two of the escape labels left by `ANF-101`. Superlinear horizontal geometry matters only if every trimming that captures `N-o(N)` points inside an `O(N)` interval leaves a discarded component with source norm of order `sqrt(N)` rather than `o(sqrt(N))`. Such a component is precisely a **source-heavy sparse tail**.

## 3. The explicit Montgomery--Taylor endpoint gives a universal tail budget

The source-heavy condition itself has a strong height cost. From `ANF-087`,

\[
g(u)=
\frac{\cos(\sqrt2u)}{\sqrt2\sin(2^{-1/2})}
\mathbf1_{[-1/2,1/2]}(u),
\qquad
J_0=g*g.
\]

Set

\[
G:=\|g\|_\infty
=\frac1{\sqrt2\sin(2^{-1/2})}.
\]

For `|alpha|<=1`, the overlap of the two support intervals in the convolution defining `J_0(alpha)` has length `1-|alpha|`. Therefore

\[
\boxed{
0\le J_0(\alpha)\le G^2(1-|\alpha|).
}
\tag{6}
\]

Let `B` be any finite conjugation-invariant multiset with

\[
m:=|B|,
\qquad
H:=\max_{z\in B}|\Im z|.
\]

For real `alpha`, every exponential has modulus at most `e^{2 pi |alpha| H}`, hence

\[
|S_B(\alpha)|\le m e^{2\pi|\alpha|H}.
\]

Using (6), for `H>0`,

\[
\begin{aligned}
\|S_B\|_0^2
&\le
2G^2m^2\int_0^1(1-\alpha)e^{4\pi H\alpha}\,d\alpha\\
&=
2G^2m^2
\frac{e^{4\pi H}-1-4\pi H}{(4\pi H)^2}.
\end{aligned}
\]

Thus

\[
\boxed{
\|S_B\|_0^2
\le
2G^2m^2
\frac{e^{4\pi H}-1-4\pi H}{(4\pi H)^2},
}
\tag{7}
\]

with the continuous `H=0` interpretation. In particular, for `H>=1`,

\[
\boxed{
\|S_B\|_0^2
\ll
m^2\frac{e^{4\pi H}}{H^2}.
}
\tag{8}
\]

The factor `H^{-2}` is the spectral endpoint effect. It comes from the **linear zero of `J_0` at `|alpha|=1`**, not from separation, cancellation, multiplicity restrictions, or a special horizontal pattern. This is why the same two logarithms that appeared in the explicit pair calculation of `ANF-095` reappear universally.

## 4. Sub-square-root tails must cross the matched log--log height scale

Apply (8) to a discarded component `B_n` of a near-extremizer `W_n`, and put

\[
L_n:=L(W_n),
\qquad
m_n:=|B_n|,
\qquad
R_n:=\frac{L_n}{m_n^2}.
\]

Assume `R_n->infinity`, equivalently `m_n=o(sqrt(L_n))`. If the tail is source-heavy in the sense that

\[
\limsup_n\frac{\|S_{B_n}\|_0^2}{L_n}>0,
\tag{9}
\]

then along a subsequence (8) forces

\[
\frac{e^{4\pi H_n}}{H_n^2}\gg R_n.
\]

Since `R_n->infinity`, necessarily `H_n->infinity`, and inversion of this elementary inequality gives

\[
\boxed{
4\pi H_n
\ge
\log R_n+2\log\log R_n+O(1).
}
\tag{10}
\]

Equivalently, if

\[
4\pi H_n
\le
\log R_n+2\log\log R_n-\omega(1),
\tag{11}
\]

then the tail is automatically source-negligible and can be removed by Section 1.

For a power-law tail `m_n=N_n^a` with fixed `a<1/2`, using `L_n\asymp N_n`, condition (10) reads

\[
4\pi H_n
\ge
(1-2a)\log N_n+2\log\log N_n+O(1).
\tag{12}
\]

This is a universal necessary condition for such a tail to remain visible in the Montgomery--Taylor source norm. It says, for example, that a bounded-height `o(sqrt(N))` collection of geometric outliers is always removable, regardless of where its real parts are placed.

## 5. The ANF-095 critical scale is the universal endpoint scale

The sparse-surgery family in `ANF-092`--`ANF-095` has total carrier size of order `n^3` and an edited block of order `n`. Hence

\[
R_n\asymp\frac{n^3}{n^2}\asymp n.
\]

Substitution into (10) gives

\[
\boxed{
4\pi H_n
\ge
\log n+2\log\log n+O(1).
}
\tag{13}
\]

This is exactly the critical height scale found in `ANF-095` from the explicit Montgomery--Taylor norm of one conjugate pair. The earlier result remains sharper for that concrete surgery because it tracks the physical edit and destination distance in detail. The present derivation shows something different: the same matched log--log scale is already forced on **every** sub-square-root source-heavy tail by the endpoint geometry of `J_0`, before its horizontal arithmetic or separable defect is examined.

This also clarifies why the coarser `cosh(2 pi H)` estimate of `ANF-094` missed the logarithmic correction. A pointwise supremum sees only `e^{4 pi H}`. The actual Montgomery--Taylor source integral pays an additional `H^{-2}` because the spectrum closes linearly at both endpoints.

## 6. Prior art, adversarial checks, and remaining frontier

The conceptual neighboring framework is concentration--compactness: minimizing or near-minimizing sequences on noncompact spaces can lose compactness through translation, vanishing, or splitting. A targeted check of that literature and generic profile-decomposition/stability results did not supply the line-specific statements (1)--(2) for the Montgomery--Taylor affine normalization, nor the explicit endpoint budget (7)--(10). No external theorem is load-bearing here. The trimming lemma is elementary Hilbert-space perturbation, and the sparse-tail threshold follows directly from the already-canonical explicit spectrum, so `SOURCES.md` is unchanged and no novelty claim is made for generic concentration--compactness principles.

The bookkeeping assumptions are deliberate. Horizontal trimming is by complete real-part fibers, so conjugation is preserved and `L(W)=L(A)+L(B)` exactly; arbitrary deletion of only part of a repeated real site would require an `O(|B|)` correction but would not change the asymptotic conclusion. The notch estimate uses only `phi_eta<=J_0`, not positivity of any spatial transform. The tail upper bound allows arbitrary multiplicities, collisions, real locations, and horizontal phase coherence; replacing the true structure factor by its maximal pointwise modulus only makes the estimate safer. Finally, (10) is asserted only when `R_n->infinity`; a tail larger than square-root scale can be source-heavy at bounded height and requires a different argument.

The fixed-notch frontier is therefore narrower than the three-way list after `ANF-101`. A dangerous sequence can no longer invoke superlinear raw diameter by itself. After source-negligible trimming, either a linearly spanned near-extremal core remains, where `ANF-101` gives normalized vertical tightness, or the discarded `o(N)` component carries macroscopic Montgomery--Taylor source norm. In the sub-square-root regime that source-heavy component must furthermore cross the universal height threshold (10). The remaining obstruction is consequently concentrated in two coupled mechanisms: **nonconvex organization of a linearly scaled tight core, or a genuinely source-heavy sparse tail capable of the macroscopic anti-alignment required by `ANF-097`**. A merely remote or geometrically extreme tail is no longer an independent escape route.