# ANF-114 — effective Montgomery--Taylor triple gap forces the optimal defect-to-span exponent

**Status:** `EXACT-DERIVED + EFFECTIVE-TRIPLE-GAP + SHARP-L^-4-SCALING + QUANTITATIVE-REAL-DILUTION + EXPONENT-SHARP-LATTICE-CALIBRATION`. `ANF-032` proves a positive compact triple gap `kappa_L` for the real Montgomery--Taylor pair kernel, but leaves its deterioration with the physical scale `L` unspecified. The additive numerator residual exposed by `CLUE-lean-residual-effective-triple-gap` makes that compactness constant explicit. For

\[
K(u)=\frac{N(u)}{D(u)},\qquad
N(u)=\cos(\pi u)-a u\sin(\pi u),\qquad
D(u)=1-2\pi^2u^2,
\]

with `a=sqrt(2) pi cot(1/sqrt(2))>0` and the removable values of `K` understood continuously, the real pair kernel is `R_MT(u)=K(u)^2`. For

\[
\kappa_L:=\inf_{\substack{u,v\ge0\\u+v\le L}}
\left(K(u)^2+K(v)^2+K(u+v)^2\right),
\]

one has the explicit bound

\[
\boxed{
\kappa_L\ge \frac{1}{16(1+2\pi^2L^2)^2}.
}
\tag{1}
\]

Positive integer triples give the converse order, hence

\[
\boxed{\kappa_L\asymp L^{-4}}\qquad(L\to\infty).
\tag{2}
\]

Inserted into the deletion theorem of `ANF-032`, (1) turns qualitative scale escape into an effective law. If a distinct real configuration `X` of `N` points has normalized Montgomery--Taylor excess `Delta(X)=Delta<1/64`, then for the explicit scale

\[
L(\Delta)=
\sqrt{\frac{(8\sqrt\Delta)^{-1}-1}{2\pi^2}}
\]

at least `N/2` points survive with no three points in an interval of length `<L/2`, and consequently

\[
\boxed{
\operatorname{diam}(X)
\ge
\frac{N-4}{8}
\sqrt{\frac{(8\sqrt\Delta)^{-1}-1}{2\pi^2}}.
}
\tag{3}
\]

Thus for `Delta->0` and large `N`, the forced span is of order `N Delta^{-1/4}`. Integer lattices have `Delta(X)asymp m^{-4}` and span `asymp Nm`, so the exponent `1/4` is optimal up to constants in this real-configuration class. This is strictly more quantitative than the linear-span requirement of `ANF-100`, but it does **not** transfer automatically to the nonreal multiset/tail geometry studied later in the analytic-frontier line because `ANF-032` uses nonnegative real pair energy.

**Provenance:** independently reconstructed and stress-tested from the local clue and canonical local findings against `main@166bf8ef98b756c8f02170ab545988802d9d74b7`. The formalization path cited by the clue was not inspected; the argument below is self-contained from the persisted kernel identity and elementary algebra.

## 1. The addition law has a robust residual form

Fix `u,v>=0` and write

\[
U=au,\qquad V=av,\qquad
s=\sin(\pi u),\qquad t=\sin(\pi v),
\]

\[
p=N(u),\qquad q=N(v),\qquad
Q=1+U^2+UV+V^2.
\tag{4}
\]

Because

\[
\cos(\pi u)=p+Us,
\qquad
\cos(\pi v)=q+Vt,
\]

the addition formulas give the exact identity

\[
\boxed{
N(u+v)=pq-Upt-Vqs-Qst.
}
\tag{5}
\]

Set

\[
A=\sqrt{1+U^2},\qquad B=\sqrt{1+V^2}.
\]

A direct factorization gives

\[
Q^2-A^2B^2
=(U+V)^2(1+U^2+V^2)\ge0,
\]

so `Q>=AB`. A second elementary inequality is

\[
UA+VB\le1+U^2+V^2\le Q.
\tag{6}
\]

Indeed `x sqrt(1+x^2)<=x^2+1/2` for `x>=0`, because squaring both nonnegative sides leaves the positive remainder `1/4`; apply it to `U` and `V` and add.

Suppose now that

\[
|p|,|q|\le\varepsilon<\frac12.
\tag{7}
\]

The unit-circle identity and triangle inequality yield

\[
1
=\| (\cos \pi u,\sin\pi u)\|_2
\le |p|+A|s|,
\]

and similarly for `v`. Hence

\[
A|s|\ge1-\varepsilon,
\qquad
B|t|\ge1-\varepsilon.
\tag{8}
\]

In particular both sines are nonzero. Equations (6)--(8) give

\[
Q|st|\ge(1-\varepsilon)^2,
\tag{9}
\]

and

\[
\begin{aligned}
|Upt|+|Vqs|
&\le \varepsilon\left(U|t|+V|s|\right)\\
&\le
\frac{\varepsilon}{1-\varepsilon}
(UA+VB)|st|\\
&\le
\frac{\varepsilon}{1-\varepsilon}Q|st|.
\end{aligned}
\tag{10}
\]

Combining (5), `|pq|<=epsilon^2`, (9), and (10),

\[
\boxed{
|N(u+v)|
\ge
(1-\varepsilon)(1-2\varepsilon)-\varepsilon^2.
}
\tag{11}
\]

At `epsilon=1/4`, the right side is `5/16`. Therefore the three numerator residuals cannot all be at most `1/4`:

\[
\boxed{
\max\{|N(u)|,|N(v)|,|N(u+v)|\}\ge\frac14.
}
\tag{12}
\]

The boundary cases `u=0` or `v=0` are even easier because `N(0)=1`; no limiting argument is needed.

## 2. The compact triple gap has exact fourth-power order

For every `0<=w<=L`,

\[
|D(w)|\le1+2\pi^2L^2.
\tag{13}
\]

Choose one of `w in {u,v,u+v}` for which (12) holds. The global identity `K(w)D(w)=N(w)` implies that this chosen `w` cannot be a removable zero of `D`: at such a point `N(w)=0`. Thus division is safe for the selected term and

\[
|K(w)|
\ge
\frac{1}{4(1+2\pi^2L^2)}.
\]

Since every term in the triple sum is nonnegative, (1) follows.

The exponent in (1) is sharp. For a positive integer `n`,

\[
K(n)=\frac{(-1)^n}{1-2\pi^2n^2},
\qquad
K(2n)=\frac{1}{1-8\pi^2n^2}.
\tag{14}
\]

If `L>=4`, take `n=floor(L/2)`, so `2n<=L` and `n>=L/4`. The admissible choice `u=v=n` gives

\[
\kappa_L
\le
\frac{2}{(1-2\pi^2n^2)^2}
+
\frac{1}{(1-8\pi^2n^2)^2}
\ll L^{-4}.
\tag{15}
\]

Together with (1), which is `gg L^{-4}` for large `L`, this proves (2). The claim is exponent/order sharp; no optimal numerical constant is asserted.

## 3. ANF-032 becomes an effective defect-to-span theorem

Let `X={x_1,...,x_N}` be a finite configuration of distinct real points and use the normalized nonnegative excess from `ANF-032`,

\[
\Delta(X)
=
\frac2N\sum_{i<j}R_{\rm MT}(x_i-x_j)
\ge0.
\tag{16}
\]

`ANF-032` proves that for any `L>0` one can delete a subset so that the survivor `Y` has at most two points in every interval of length `<L/2`, with

\[
\frac{|X\setminus Y|}{N}
\le
\frac{2\Delta(X)}{\kappa_L}.
\tag{17}
\]

Using (1),

\[
\boxed{
\frac{|X\setminus Y|}{N}
\le
32\Delta(X)(1+2\pi^2L^2)^2.
}
\tag{18}
\]

Assume `0<Delta<1/64` and choose

\[
1+2\pi^2L^2=\frac{1}{8\sqrt\Delta}.
\tag{19}
\]

Then the right side of (18) is `1/2`, so `m:=|Y|>=N/2`. Order the survivors as

\[
y_1<\cdots<y_m.
\]

The local two-point property implies

\[
y_{i+2}-y_i\ge\frac L2.
\tag{20}
\]

Summing disjoint two-step gaps gives

\[
\operatorname{diam}(Y)
\ge
\frac{(m-2)L}{4}
\ge
\frac{(N-4)L}{8}.
\tag{21}
\]

Since `diam(X)>=diam(Y)`, equations (19)--(21) prove (3). Moreover

\[
L(\Delta)
\sim\frac{1}{4\pi}\Delta^{-1/4}
\qquad(\Delta\downarrow0),
\tag{22}
\]

so, away from the irrelevant `N-4` endpoint correction,

\[
\boxed{
\operatorname{diam}(X)\gg N\Delta(X)^{-1/4}.
}
\tag{23}
\]

This provides the growing-scale modulus that `ANF-032` explicitly left open and strengthens `ANF-100` inside the distinct-real subclass from a merely linear lower bound to a defect-sensitive one.

## 4. Integer lattices make the exponent optimal

Take

\[
X_{N,m}=\{0,m,2m,\ldots,(N-1)m\},
\qquad N\ge2,
\qquad m\in\mathbb N.
\tag{24}
\]

Using (14), its excess is

\[
\Delta(X_{N,m})
=
\frac2N
\sum_{k=1}^{N-1}(N-k)K(mk)^2.
\tag{25}
\]

For the upper bound, since `mk>=1`,

\[
2\pi^2m^2k^2-1
\ge
(2\pi^2-1)m^2k^2,
\]

and therefore

\[
\begin{aligned}
\Delta(X_{N,m})
&\le
\frac{2}{(2\pi^2-1)^2m^4}
\sum_{k=1}^{\infty}k^{-4}\\
&\le
\frac{8}{3(2\pi^2-1)^2m^4}.
\end{aligned}
\tag{26}
\]

The first lag gives the missing converse estimate:

\[
\begin{aligned}
\Delta(X_{N,m})
&\ge
2\left(1-\frac1N\right)K(m)^2\\
&\ge
\frac{1}{4\pi^4m^4}.
\end{aligned}
\tag{27}
\]

Hence, uniformly for `N>=2`,

\[
\boxed{
\Delta(X_{N,m})\asymp m^{-4}.
}
\tag{28}
\]

But

\[
\operatorname{diam}(X_{N,m})=(N-1)m.
\tag{29}
\]

Thus `diam(X)asymp N Delta^{-1/4}` along this family for large `N`, up to constants. Any universal lower bound with a larger exponent than `1/4` would fail as `m->infinity`. The fourth-power deterioration of `kappa_L` and the fourth-root defect-to-span law are therefore the correct scales for the present real problem.

## 5. Adversarial checks, prior art, and scope

The proof does not divide blindly through the removable singularities of `D`. Equation `K D=N` is used first; the term selected by (12) has nonzero numerator and hence cannot lie at a zero of `D`. The signs in (5) were reconstructed directly from the addition formulas, and the only place `u,v>=0` is essential is (6), through `U,V>=0`. The threshold `epsilon=1/4` is deliberately nonoptimal: it certifies a clean constant while leaving the exact best triple-gap constant open.

The large-`L` upper calibration requires only `L>=4`, so (2) is an asymptotic statement. Equation (3) is meaningful as a growing-span assertion for small positive defect and sufficiently large `N`; `Delta=0` is handled by the already stronger exact zero-set rigidity rather than by substituting into `L(Delta)`. The lattice family establishes exponent sharpness, not equality in (1) or optimal constants in (3).

A targeted prior-art search checked the Hilbert-space pair-correlation literature around the Montgomery--Taylor extremizer, including the Carneiro--Chandee--Littmann--Milinovich extremal-function framework and the 2026 Montgomery--Taylor application to simple zeta zeros. It did not locate this additive-residual modulus, the explicit `kappa_L asy L^-4` stability law, or the resulting `Delta^{-1/4}` real-configuration span theorem. That search outcome is not a global novelty claim. No external theorem is load-bearing in the derivation, so `SOURCES.md` does not change.

The main scope boundary is structural. The implication from small Montgomery--Taylor excess to deletions in `ANF-032` uses a nonnegative pair energy for **distinct real configurations**. `ANF-100` and the later sparse-tail cascade address conjugation-invariant complex multisets, where cancellation and affine multiplicity terms re-enter. Equation (23) therefore sharpens the real finite-configuration face and the scale-escape obstruction feeding it; it does not by itself close the current complex escape regimes.

## 6. Research consequence

`CLUE-lean-residual-effective-triple-gap` is supported and resolved by this finding. Its main candidate lower bound is valid, and the lattice calibration can be strengthened from a one-sided `Delta=O(m^-4)` estimate to the two-sided law `Delta asy m^-4`, which proves the exponent sharpness cleanly.

The useful new invariant is now explicit: in the all-real Montgomery--Taylor closure, a configuration can approach the sharp face only by diluting on a physical scale at least proportional to `Delta^{-1/4}` per particle, and that rate cannot be improved without adding hypotheses beyond the pair kernel. The next genuine question is no longer the decay rate of the real triple gap. It is whether any analogue of this effective modulus survives the complex/conjugate geometry strongly enough to constrain the source-unsaturated sparse packets left by `ANF-113`.