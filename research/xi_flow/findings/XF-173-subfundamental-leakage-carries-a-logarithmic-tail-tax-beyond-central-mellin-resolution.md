---
type: theorem
research_line: xi_flow
finding_id: XF-173
status: canonical
---

# XF-173 — Subfundamental leakage carries a logarithmic tail tax beyond central Mellin resolution

**Evidence classification:** `EXACT-DERIVED + ASYMPTOTIC-SEPARATION + ADVERSARIAL-STRESS`. Inside the normalized positive even common Xi scale-mixture gauge, the XF-172 subfundamental leakage has an exact one-variable kernel. It agrees with the XF-171 central Mellin deficit for sufficiently small shifts, but remote shifts are charged by an additional logarithmic factor. Consequently the leakage can be infinite while the Mellin deficit is arbitrarily small. No external theorem is load-bearing.

## Statement

Let `nu` be a finite positive even Borel measure on `R` satisfying

\[
\int_{\mathbb R}\cosh a\,d\nu(a)=1.
\tag{1}
\]

Retain the XF-171 central Mellin deficit

\[
d_\nu=\int_{\mathbb R}(\cosh a-1)\,d\nu(a)
\tag{2}
\]

and the XF-172 weighted subfundamental leakage

\[
\mathcal L_\nu=
\int_{(0,\pi)}
\left[
\left(\frac{\pi}{\lambda}\right)^{1/4}-1
\right]^2 d\mu_\nu(\lambda),
\tag{3}
\]

where

\[
\mu_\nu=
\int_{\mathbb R}e^a
\sum_{n\ge1}\delta_{\pi n^2e^{4a}}\,d\nu(a).
\tag{4}
\]

For `b>0`, define

\[
N(b):=\lceil e^{2b}\rceil-1
\tag{5}
\]

and

\[
\boxed{
K(b):=
 e^{-b}\sum_{1\le n<e^{2b}}
\left(\frac{e^b}{\sqrt n}-1\right)^2.
}
\tag{6}
\]

Then

\[
\boxed{
\mathcal L_\nu=\int_{(0,\infty)}K(b)\,d\nu(b).
}
\tag{7}
\]

If

\[
H_N:=\sum_{n\le N}\frac1n,
\qquad
H_N^{(1/2)}:=\sum_{n\le N}\frac1{\sqrt n},
\tag{8}
\]

then exactly

\[
\boxed{
K(b)=e^bH_{N(b)}-2H_{N(b)}^{(1/2)}+N(b)e^{-b}.
}
\tag{9}
\]

For small displacement,

\[
0<b\le\frac12\log2
\quad\Longrightarrow\quad
\boxed{K(b)=2(\cosh b-1).}
\tag{10}
\]

For remote displacement,

\[
\boxed{
K(b)=2b e^b+O(e^b),
\qquad b\to\infty.
}
\tag{11}
\]

The positive-half kernel of `d_nu` is

\[
D(b):=2(\cosh b-1)=e^b+e^{-b}-2,
\tag{12}
\]

so

\[
\boxed{
\frac{K(b)}{D(b)}=2b+O(1).
}
\tag{13}
\]

Hence

\[
\boxed{
\mathcal L_\nu<\infty
\iff
\int_1^\infty b e^b\,d\nu(b)<\infty.
}
\tag{14}
\]

Normalization `(1)` only forces the corresponding `e^b` moment. The extra factor `b` is a genuine logarithmic tail tax.

Moreover, for every `eta>0` there exists a normalized positive even `nu` such that

\[
\boxed{
0<d_\nu<\eta,
\qquad
\mathcal L_\nu=+\infty.
}
\tag{15}
\]

Thus there is no universal finite-valued upper bound on `mathcal L_nu` in terms of `d_nu` alone on the unbounded common-scale gauge. XF-172's inequality `d_nu <= mathcal L_nu` remains valid, but the two source metrics are not equivalent.

## 1. Exact leakage kernel

Only negative common shifts can place an Xi square-lattice atom below `pi`. Write such a shift as `a=-b`, `b>0`. Its `n`th atom is

\[
\lambda_{n,b}=\pi n^2e^{-4b}
\tag{16}
\]

with Laplace mass factor `e^{-b}`. It lies below `pi` exactly when

\[
n<e^{2b}.
\tag{17}
\]

At that atom the XF-172 weight is

\[
\left[
\left(\frac{\pi}{\lambda_{n,b}}\right)^{1/4}-1
\right]^2
=
\left(\frac{e^b}{\sqrt n}-1\right)^2.
\tag{18}
\]

All terms are nonnegative, so Tonelli and evenness of `nu` give `(7)`. Expanding `(6)` yields

\[
\begin{aligned}
K(b)
&=e^{-b}\sum_{n\le N(b)}
\left(\frac{e^{2b}}n-\frac{2e^b}{\sqrt n}+1\right)\\
&=e^bH_{N(b)}-2H_{N(b)}^{(1/2)}+N(b)e^{-b},
\end{aligned}
\tag{19}
\]

which proves `(9)`.

If `0<b<=(1/2)log 2`, only `n=1` satisfies `(17)`, and therefore

\[
K(b)=e^{-b}(e^b-1)^2=e^b+e^{-b}-2=2(\cosh b-1).
\tag{20}
\]

This explains the exact equality `mathcal L=d` in the sufficiently small XF-167/XF-172 three-atom stress family: before the `n=2` copy crosses the spectral edge, the first theta atom pays exactly the whole Mellin deficit and there is no higher-atom surcharge.

## 2. Remote shifts pay one extra logarithmic moment

As `b->infinity`,

\[
N(b)=e^{2b}+O(1).
\tag{21}
\]

Elementary sum-integral comparison gives

\[
H_N=\log N+O(1),
\qquad
H_N^{(1/2)}=2\sqrt N+O(1).
\tag{22}
\]

Substitution into `(9)` gives `(11)`. Since `D(b)=e^b(1+o(1))`, equation `(13)` follows. In particular there exist constants `b_0,c,C>0` such that

\[
c\,b e^b\le K(b)\le C\,b e^b,
\qquad b\ge b_0.
\tag{23}
\]

The kernel is bounded on every compact `b` interval, so `(23)` proves `(14)`. By contrast, normalization and evenness only give

\[
\int_0^\infty e^b\,d\nu(b)
\le2\int_0^\infty\cosh b\,d\nu(b)<\infty.
\tag{24}
\]

Thus finite `mathcal L_nu` requires strictly stronger tail integrability than the common-mixture gauge itself.

On the spectral side this has a simple interpretation: the test weight in `(3)` behaves like `(pi/lambda)^(1/2)` as `lambda->0`. It is an unbounded edge observable. Tiny amounts of source mass transported to exponentially small spectral scales can therefore contribute little to `d_nu` while producing arbitrarily large leakage.

For compact shift support the mismatch is mild. Equations `(10)` and `(13)`, plus boundedness on compact intervals, imply a universal constant `C_0` such that support in `|a|<=B` gives

\[
\mathcal L_\nu\le C_0(1+B)d_\nu.
\tag{25}
\]

So XF-172 is locally sharp and differs from XF-171 by at most a logarithmic-radius factor on bounded gauges. The strong separation is an unbounded-tail phenomenon.

## 3. Stress family: small `d_nu`, infinite `mathcal L_nu`

Choose an integer `k_0` large enough that the lower bound in `(23)` holds for every integer `k>=k_0`, and set

\[
C_*:=\sum_{k\ge k_0}\frac{e^{-k}\cosh k}{k^2}<\infty.
\tag{26}
\]

For `0<epsilon<C_*^{-1}`, define

\[
q_k:=\epsilon\frac{e^{-k}}{k^2},
\qquad
m_0:=1-\epsilon C_*,
\tag{27}
\]

and

\[
\boxed{
\nu_\epsilon
=m_0\delta_0+
\sum_{k\ge k_0}\frac{q_k}{2}(\delta_k+\delta_{-k}).
}
\tag{28}
\]

Then

\[
\int\cosh a\,d\nu_\epsilon(a)=1.
\tag{29}
\]

Its central deficit is

\[
d_{\nu_\epsilon}
=
\epsilon\sum_{k\ge k_0}
\frac{e^{-k}(\cosh k-1)}{k^2}
=:\epsilon C_1,
\tag{30}
\]

with `0<C_1<infinity`, so `d_(nu_epsilon)->0` linearly as `epsilon->0`. But `(7)` and `(23)` imply

\[
\begin{aligned}
\mathcal L_{\nu_\epsilon}
&=\frac{\epsilon}{2}
\sum_{k\ge k_0}\frac{e^{-k}}{k^2}K(k)\\
&\ge\frac{c\epsilon}{2}
\sum_{k\ge k_0}\frac1k
=+\infty.
\end{aligned}
\tag{31}
\]

This proves `(15)`.

The zero-resolution stress is stronger than merely showing nonequivalent norms. Given any finite `T`, choose `epsilon` so that

\[
d_{\nu_\epsilon}<\frac1{4T^2+2}.
\tag{32}
\]

XF-171 then certifies that the common-mixture multiplier has no zero anywhere in the critical strip through height `T`, while XF-172's leakage quantity is infinite. Thus `mathcal L_nu` is a valid source-visible sufficient modulus but can be infinitely more pessimistic than the intrinsic finite-height modulus on unbounded mixtures.

## 4. Consequence for the source-resolution frontier

XF-172 proposed deriving `mathcal L_nu=o(T^-2)` from a natural quantitative approximation to the single Xi square lattice. XF-173 shows that this target silently includes a tail regularity hypothesis: any such reconstruction theorem must control the logarithmically reinforced moment

\[
\int b e^b\,d\nu(b),
\tag{33}
\]

not merely the normalized exponential moment or `d_nu`. A topology that sees only bounded spectral test functions cannot by itself control this unbounded edge observable; a uniform-integrability input is needed.

The live common-gauge gate therefore splits in two. One route is to derive the required logarithmic tail control from genuine theta-source reconstruction data, in which case XF-172 remains the right source-visible bridge. The other is to find a bounded or regularized source-visible spectral observable that still controls `d_nu` at the `o(T^-2)` scale required by XF-171 without paying the extra factor `b`. If neither route is natural, further metric refinement inside the common-scale gauge has little value and the line should move to atomwise/mesoscopic deformation of the individual `pi n^2` atoms.

The conclusion is deliberately narrow: **spectral-edge visibility and finite-height zero resolution induce different tail topologies once arbitrarily remote common-scale contamination is allowed.**

## Prior-art and novelty audit

The closest general functional-analytic phenomenon found in the audit is standard: weak convergence controls bounded continuous observables, while unbounded moments need additional uniform-integrability hypotheses. Positive Laplace representations of completely monotone functions are also classical. Neither supplies the theta-specific exact kernel `(6)` or its asymptotic ratio `(13)`.

No external theorem is used in the proof. The kernel identity follows directly from XF-169/XF-172 and positivity; `(11)` uses only elementary sum-integral estimates; the stress family is explicit. Therefore `SOURCES.md` requires no new load-bearing anchor, and no broad novelty claim is made beyond the Mathia source-resolution framework.

## Falsification boundary

Positivity and evenness remain load-bearing because they define the XF-169 gauge and permit the one-sided kernel representation. The theorem concerns unbounded common shifts and does not weaken XF-172 for compactly supported or logarithmically uniformly integrable families.

The stress family does not create a low-height zero. It shows instead that XF-172's sufficient source metric can diverge while XF-171 still proves a large zero-free window. The theorem therefore separates two resolution metrics; it does not refute either theorem.

Finally, nothing here automatically extends to atomwise perturbations of the individual square-lattice atoms. Those deformations do not admit one common shift law `nu` and require a different spectral budget.

## Relation to prior findings

XF-169 classifies normalized positive common scale mixing. XF-170 gives the sharp compact-support displacement law. XF-171 gives the compact-support-free central Mellin-defect law. XF-172 makes that defect source-visible through subfundamental spectral leakage and is exactly sharp for sufficiently small displacement.

XF-173 supplies the missing adversarial comparison: the XF-172 kernel equals the deficit kernel locally but grows like `2b` times it in the tail. The source bridge is therefore locally exact and globally stronger by one logarithmic shift moment.

## Consequence for `xi_flow`

Do not treat `mathcal L_nu=o(T^-2)` as a topology-free consequence of approximate square-lattice agreement. On unbounded common mixtures it is a useful theorem target only when the approximation also controls the `b e^b` tail. Otherwise use the intrinsic `d_nu T^2` modulus of XF-171, seek a bounded source-visible surrogate for `d_nu`, or move to the genuinely different atomwise/mesoscopic regime.