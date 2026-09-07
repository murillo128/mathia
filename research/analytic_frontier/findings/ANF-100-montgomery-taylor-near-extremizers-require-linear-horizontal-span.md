# ANF-100 — Montgomery--Taylor near-extremizers require linear horizontal span

**Status:** `EXACT-DERIVED + ALL-COMPLEX-MULTISETS + HORIZONTAL-DENSITY-BARRIER + NEAR-EXTREMIZER-SCALE-ESCAPE + NOTCH-ENVELOPE-FRONTIER`. `ANF-087`--`ANF-099` reduce the remaining central-notch obstruction to growing physical Montgomery--Taylor near-extremizers whose source-generated tensor can keep anomalously large notch exposure. A first geometry constraint is available without any Gram conditioning, separation, height bound, or separable-carrier selection: conjugation symmetry makes every vertical orbit contribute a **positive** amplitude after its horizontal phase is factored out. Therefore all terms are phase-aligned on a frequency interval whose width is the reciprocal of the total horizontal span. The Montgomery--Taylor source norm must pay for that coherent central interval.

Let

\[
J_0:=J_{\rm MT},\qquad
S_W(\alpha):=\sum_{z\in W}e^{-2\pi i\alpha z},
\qquad
N:=|W|,
\]

for a nonempty finite conjugation-invariant multiset `W`, and write

\[
L(W):=2N-\sigma(W),
\qquad
r(W):=\frac{\int_{-1}^{1}J_0(\alpha)|S_W(\alpha)|^2\,d\alpha}{L(W)}.
\tag{1}
\]

Define its horizontal diameter

\[
D_x(W):=\max_{z\in W}\Re z-\min_{z\in W}\Re z.
\tag{2}
\]

For every fixed `0<a_0<1` put

\[
j(a_0):=\min_{|\alpha|\le a_0}J_0(\alpha)>0.
\tag{3}
\]

Then for every `0<\vartheta<\pi/2`, with the convention `\vartheta/(\pi D_x)=+\infty` when `D_x=0`, one has the exact lower bound

\[
\boxed{
 r(W)
 \ge
 j(a_0)\cos^2\!\vartheta\;N
 \min\!\left\{a_0,\frac{\vartheta}{\pi D_x(W)}\right\}.
}
\tag{4}
\]

Consequently every family with `r(W)\le1+\varepsilon` satisfies

\[
\boxed{
N
\le
\frac{1+\varepsilon}{j(a_0)\cos^2\vartheta}
\max\!\left\{\frac1{a_0},\frac{\pi D_x(W)}{\vartheta}\right\}.
}
\tag{5}
\]

In particular, if `W_n` is Montgomery--Taylor near-extremal and `N_n:=|W_n|\to\infty`,

\[
r(W_n)\to1,
\]

then

\[
\boxed{
\liminf_{n\to\infty}\frac{D_x(W_n)}{N_n}
\ge
c_*J_0(0),
\qquad
c_*:=\max_{0<\vartheta<\pi/2}
\frac{\vartheta\cos^2\vartheta}{\pi}.
}
\tag{6}
\]

The maximizer is the unique solution of

\[
2\vartheta\tan\vartheta=1,
\]

so

\[
c_*=0.1311275283\ldots.
\tag{7}
\]

For the explicit Montgomery--Taylor factor from `ANF-087`,

\[
J_0(0)
=\int_{-1/2}^{1/2}g(u)^2\,du
=\frac{1+\sin(\sqrt2)/\sqrt2}
       {4\sin^2(2^{-1/2})}
=1.0061271908\ldots,
\tag{8}
\]

and hence the asymptotic numerical consequence is

\[
\boxed{
\liminf_{n\to\infty}\frac{D_x(W_n)}{N_n}
\ge0.1319309717\ldots.
}
\tag{9}
\]

Thus a high-cardinality physical near-extremizer cannot hide inside a bounded or sublinear horizontal window, no matter how large or irregular its imaginary parts are. Any obstruction to the `ANF-099` notch-exposure criterion must use genuine linear-scale horizontal escape before the harder nonconvex anti-alignment issue of `ANF-097` even becomes relevant.

## 1. Conjugation turns every vertical orbit into a positive amplitude

Group `W` by horizontal center. A real site `x` of multiplicity `m` contributes

\[
m e^{-2\pi i\alpha x}.
\tag{10}
\]

A nonreal orbit `x+iy,x-iy`, with multiplicity `m` on each side, contributes for real `alpha`

\[
m e^{-2\pi i\alpha(x+iy)}
+m e^{-2\pi i\alpha(x-iy)}
=
2m\cosh(2\pi\alpha y)e^{-2\pi i\alpha x}.
\tag{11}
\]

After combining all vertical levels at a common center, therefore,

\[
S_W(\alpha)
=\sum_x A_x(\alpha)e^{-2\pi i\alpha x},
\qquad
A_x(\alpha)>0,
\tag{12}
\]

and, crucially,

\[
\boxed{
\sum_x A_x(\alpha)\ge N
\qquad(\alpha\in\mathbb R),
}
\tag{13}
\]

because every `cosh` factor is at least one. Large imaginary heights cannot reduce the coherent central mass; they only increase the positive orbit amplitudes before horizontal phases are summed.

Let `c` be the midpoint of the smallest interval containing all real parts of points of `W`. Then

\[
|x-c|\le\frac{D_x(W)}2.
\tag{14}
\]

If

\[
|\alpha|\le\frac{\vartheta}{\pi D_x(W)},
\tag{15}
\]

then every phase after multiplication by the harmless common factor `e^{2 pi i alpha c}` obeys

\[
|2\pi\alpha(x-c)|\le\vartheta.
\tag{16}
\]

All vectors in (12) therefore lie in the same cone of half-angle `vartheta`. Taking the real part along its axis and using (13) gives

\[
\boxed{
|S_W(\alpha)|
\ge
\cos\vartheta\sum_xA_x(\alpha)
\ge N\cos\vartheta.
}
\tag{17}
\]

This is the load-bearing observation. It uses positivity of the **physical conjugacy-orbit coefficients**, not positivity of an arbitrary signed exponential sum. It is therefore unaffected by the bad signed Rayleigh directions of `ANF-090`--`ANF-093`.

## 2. The coherent central interval forces the density bound

Set

\[
a:=\min\!\left\{a_0,\frac{\vartheta}{\pi D_x(W)}\right\}.
\tag{18}
\]

On `[-a,a]`, equations (3) and (17) imply

\[
J_0(\alpha)|S_W(\alpha)|^2
\ge
j(a_0)N^2\cos^2\vartheta.
\tag{19}
\]

Hence

\[
\int_{-1}^{1}J_0|S_W|^2
\ge
2a\,j(a_0)N^2\cos^2\vartheta.
\tag{20}
\]

The affine denominator satisfies only

\[
L(W)=2N-\sigma(W)\le2N.
\tag{21}
\]

Dividing (20) by (21) proves (4). If `r(W)<=1+epsilon`, rearranging (4) gives (5).

The result is deliberately insensitive to the simple-real bookkeeping: replacing `L(W)` by its largest possible value `2N` only weakens the lower bound. Repeated real sites, collisions, multiple vertical levels at one center, and arbitrary nonreal heights are all included without separate cases.

## 3. Optimizing the phase cone gives the asymptotic constant

Suppose `N_n->infinity` and `r(W_n)->1`. For every fixed `a_0 in (0,1)` and fixed `vartheta in (0,pi/2)`, equation (5) eventually cannot be satisfied by the `1/a_0` branch. Thus

\[
\liminf_n\frac{D_x(W_n)}{N_n}
\ge
\frac{j(a_0)}{\pi}\,
\vartheta\cos^2\vartheta.
\tag{22}
\]

Now send `a_0 downarrow0`. Continuity of `J_0` gives

\[
j(a_0)\longrightarrow J_0(0).
\tag{23}
\]

The one-variable function `vartheta cos^2(vartheta)` has derivative

\[
\cos^2\vartheta-2\vartheta\sin\vartheta\cos\vartheta,
\tag{24}
\]

so its interior maximum is characterized by `2 vartheta tan(vartheta)=1`. This proves (6)--(7).

For completeness, `ANF-087` gives

\[
g(u)=
\frac{\cos(\sqrt2u)}{\sqrt2\sin(2^{-1/2})}
\mathbf1_{[-1/2,1/2]}(u),
\qquad
J_0=g*g.
\tag{25}
\]

Because `g` is even,

\[
J_0(0)=\int g(u)^2\,du.
\tag{26}
\]

Integrating `cos^2(sqrt2 u)` on `[-1/2,1/2]` gives (8), and multiplication by `c_*` gives (9).

## 4. Consequence for the notch-exposure frontier

`ANF-099` shows that the existence of an improving amplitude along one frozen central-notch ray is equivalent to

\[
\beta_\eta<B_\eta,
\tag{27}
\]

where `beta_eta` is the maximal limiting notch exposure among Montgomery--Taylor near-extremizers. Its abstract control tensor in `ANF-099` can concentrate like a Fejer kernel at the spectral origin. Equation (6) identifies a necessary piece of any **physical** realization of that behavior: if its cardinality tends to infinity, its horizontal geometry must expand on at least a linear scale.

This removes several tempting but invalid counterexample mechanisms. A growing vertical stack over `O(1)` horizontal centers cannot be near-extremal. Neither can a high-cardinality complex cluster whose real parts occupy `o(N)` total span, regardless of how its heights or Gram conditioning are tuned. In particular, vertical growth cannot substitute for horizontal escape in the source norm, because the conjugate pairing makes vertical growth positive on the coherent central interval.

The result does **not** prove `beta_eta<B_eta`. Linear horizontal span is compatible with the arithmetic finite-difference constructions behind `ANF-090`--`ANF-096`, and with the abstract Fejer scale used as the negative control in `ANF-099`. It also gives only a global diameter constraint, not a minimum gap, a local Beurling-density bound, a separable comparator, or a favorable source-interference sign. The surviving problem remains to use the physical positive-multiset structure at this linear escape scale strongly enough to bound the contracted tensor exposure or to construct a genuine obstruction.

## 5. Prior art, adversarial audit, and evidence boundary

The neighboring harmonic-analysis literature contains much stronger lower-frame and density statements for exponential systems under additional hypotheses. Classical Ingham/nonharmonic-Fourier inequalities and the Montgomery--Vaughan large sieve exploit frequency separation; Turan--Nazarov/Remez inequalities control concentration of general exponential polynomials with constants depending on the number of terms and spectral geometry. Those are useful comparisons, but none is imported here. Equation (17) is an elementary positive-cone estimate special to conjugation-invariant **positive multisets**, and (4) follows directly from the already-canonical Montgomery--Taylor spectrum. No new external theorem is load-bearing, so `SOURCES.md` is unchanged.

The adversarial checks are direct. Horizontal translation contributes only a common unimodular phase and leaves (17) unchanged. Nonreal heights cannot reverse a coefficient because they enter through `cosh`; arbitrary multiplicity only increases the positive amplitude in (13). The interval in (18) is kept inside a fixed compact subset of `(-1,1)`, where `J_0` has a strictly positive minimum. No pointwise sign of the spatial transform `K^2` is used for complex arguments, and no pairwise decomposition is invoked, so the complex cancellation issues that block several earlier spatial arguments do not enter.

The bound is intentionally one-sided. It rules out sublinear horizontal support for growing near-extremizers but does not say that a linearly spread configuration is near-extremal, nor that its notch exposure is small. A decisive falsification of the next step would be an explicit physical sequence with `r(W_n)->1`, `D_x(W_n)=Theta(N_n)`, and notch exposure tending to `B_eta` or above. A decisive positive continuation would show that the exact projection taxes of `ANF-088`, together with the linear-scale horizontal geometry forced here, prevent such concentration.