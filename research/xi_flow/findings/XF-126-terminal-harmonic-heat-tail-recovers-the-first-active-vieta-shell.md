# XF-126 — terminal harmonic heat tail recovers the first active Vieta shell

**Status:** `EXACT-DERIVED` + `STRUCTURAL/POSITIVE-BOUNDARY` + `TERMINAL-HARMONIC` + `GLOBAL-OBSERVABLE` + `COLLISION-ADVERSARY-SEPARATION`. XF-125 shows that every sublinear collection of **proper** harmonic heat histories can remain identically blind while a fraction `1-o(1)` of a periodic divisor sits in double collisions. Its proof also identifies the sharp algebraic place where that semigroup construction stops: the total-degree relation itself forces the terminal harmonic `m=N` into the nonlinear support cascade.

That boundary is genuine. The terminal power-sum history is not another sparse coordinate. On any unit-circle target slice it contains a global Vieta tail that recovers the first nonzero interior Vieta shell and its magnitude. More precisely, let

\[
E(z,0)=\prod_{j=1}^N(1+\nu_j z)
      =\sum_{k=0}^N E_k z^k,
\qquad |\nu_j|=1,
\tag{1}
\]

and evolve by the exact XF-067 periodic coefficient heat flow

\[
E_k(s)=E_k\,e^{-\delta_k s},
\qquad
\delta_k:=\frac{4\pi^2}{L^2}k(N-k),
\qquad s\ge0.
\tag{2}
\]

The unit-circle target slice gives

\[
|E_N|=1,
\qquad
E_{N-k}=E_N\overline{E_k}.
\tag{3}
\]

Write

\[
P_m(s):=\sum_{j=1}^N\nu_j(s)^m
\tag{4}
\]

at coefficient level through Newton identities, so this remains defined after collisions or complex-root intervals. If the divisor is not a rotated regular `N`-gon, define the first active Vieta shell

\[
r:=\min\left\{1\le k\le\left\lfloor\frac N2\right\rfloor:E_k\ne0\right\}.
\tag{5}
\]

Then for some `eta>0`,

\[
\boxed{
\frac{(-1)^{N-1}P_N(s)}{N E_N}
=
1-\kappa_r|E_r|^2e^{-2\delta_r s}
+O\!\left(e^{-(2\delta_r+\eta)s}\right),
}
\tag{6}
\]

where

\[
\kappa_r=
\begin{cases}
1,&2r<N,\\[2mm]
\tfrac12,&2r=N.
\end{cases}
\tag{7}
\]

Consequently the **single scalar history** `P_N(s)` determines both the first active shell index and its magnitude:

\[
\boxed{
\delta_r
=-\frac12\lim_{s\to\infty}
\frac1s
\log\left|
1-\frac{(-1)^{N-1}P_N(s)}{N E_N}
\right|,
}
\tag{8}
\]

and, after `r` is identified from `delta_r`,

\[
\boxed{
\kappa_r|E_r|^2
=
\lim_{s\to\infty}
e^{2\delta_r s}
\left(
1-\frac{(-1)^{N-1}P_N(s)}{N E_N}
\right).
}
\tag{9}
\]

In particular,

\[
\boxed{
P_N(s)\ \text{is constant for }s\ge0
\iff
E_1=\cdots=E_{N-1}=0
\iff
\{\nu_j\}_{j=1}^N\ \text{is a rotated regular }N\text{-gon}.
}
\tag{10}
\]

Thus the terminal mode is a genuine global observable: every nonregular unit-circle divisor leaves a nonzero asymptotic heat signature in `P_N`, no matter how many proper harmonics vanish identically.

## 1. Newton's logarithm turns the terminal mode into a weighted Vieta partition sum

The standard generating identity is

\[
\log E(z,s)
=
\sum_{m\ge1}(-1)^{m-1}\frac{P_m(s)}m z^m.
\tag{11}
\]

Hence

\[
\frac{(-1)^{N-1}P_N(s)}N
=[z^N]\log E(z,s).
\tag{12}
\]

Under `(2)`, every monomial contributing to the coefficient on the right corresponds to a composition

\[
k_1+\cdots+k_j=N,
\qquad
1\le k_i\le N,
\tag{13}
\]

and carries heat exponent

\[
D(k_1,\ldots,k_j)
:=\delta_{k_1}+\cdots+\delta_{k_j}.
\tag{14}
\]

The one-part contribution is simply `E_N`, whose rate is zero. Every positive-rate contribution uses at least two proper Vieta indices.

Let

\[
\alpha:=\frac{4\pi^2}{L^2},
\qquad
\delta_k=\alpha k(N-k).
\tag{15}
\]

For positive `a,b` with `a+b<=N`,

\[
\boxed{
\delta_a+\delta_b
=\delta_{a+b}+2\alpha ab.
}
\tag{16}
\]

Thus splitting one Vieta index into two strictly increases the total heat exponent. Because `(3)` makes the proper support symmetric and `r` is the smallest active index on the lower half, the smallest positive exponent among all compositions `(13)` is therefore

\[
\boxed{2\delta_r,}
\tag{17}
\]

and it comes uniquely from the pair `(r,N-r)`; when `2r=N`, this is the repeated central pair `(r,r)`. Every other contributing composition has exponent at least `2 delta_r+eta` for some positive finite spectral gap `eta` depending on the fixed divisor.

The quadratic term `-Z^2/2` in `log(1+Z)` now gives the coefficient explicitly. If `2r<N`, the two orderings of `(r,N-r)` combine to

\[
-E_rE_{N-r}e^{-2\delta_r s}
=-E_N|E_r|^2e^{-2\delta_r s}.
\tag{18}
\]

If `2r=N`, only one quadratic monomial occurs and its coefficient is

\[
-\frac12E_r^2e^{-2\delta_r s}
=-\frac12E_N|E_r|^2e^{-2\delta_r s}.
\tag{19}
\]

Equations `(12)`, `(18)`, and `(19)` are exactly `(6)`. No root separation, simplicity, or perturbative approximation is used; the only target-slice input is unit-circle self-inversivity `(3)` and the exact diagonal coefficient flow of XF-067.

## 2. The heat tail is an exact first-shell spectroscopy

Equation `(6)` has two pieces of information that proper sparse histories do not possess. First, the decay exponent gives `delta_r`. Since `k(N-k)` is strictly increasing for `1<=k<=N/2`, this determines `r` uniquely. Second, self-inversivity turns the leading quadratic coefficient into the positive quantity `|E_r|^2` after normalization by `E_N`; there is no phase cancellation available at the first active shell.

This also gives a useful relative form. Consider two unit-circle target states with Vieta coordinates `E_k` and `\widetilde E_k`. Suppose

\[
E_N=\widetilde E_N,
\qquad
E_k=\widetilde E_k
\quad(1\le k<r),
\tag{20}
\]

and let `r<=N/2` be the first lower-half shell at which they may differ. By `(3)` the corresponding upper-half shells below `N-r` agree as well. After subtracting the two terminal histories, every contribution built only from the common lower shells cancels. The first possible noncommon quadratic pair is `(r,N-r)`, so whenever

\[
|E_r|\ne|\widetilde E_r|,
\tag{21}
\]

one has

\[
\boxed{
\frac{(-1)^{N-1}}N
\bigl(P_N(s)-\widetilde P_N(s)\bigr)
=
-\kappa_rE_N
\bigl(|E_r|^2-|\widetilde E_r|^2\bigr)
e^{-2\delta_r s}
+o(e^{-2\delta_r s}).
}
\tag{22}
\]

Hence equal terminal histories force equality of the first differing shell magnitude. This is not yet full observability of the divisor—the phases of later shells can still enter grouped nonlinear exponentials—but it is already enough to break the collision/simple matched pair used in XF-125.

## 3. The XF-125 collision crystal cannot also hide the terminal history

Recall the XF-125 controls

\[
F_N(w)=Q_{R,u}(w)^2Q_{d,v}(w),
\qquad
G_N(w)=Q_{R,u_1}(w)Q_{R,u_2}(w)Q_{d,v}(w),
\tag{23}
\]

with

\[
Q_{r,u}(w)=w^r-u,
\qquad
2R+d=N,
\qquad
d=o(N),
\qquad
u\text{-supports pairwise disjoint for }G_N.
\tag{24}
\]

Up to the harmless parity phase converting `w^r-u` into the elementary-symmetric generating factor, write the unit amplitudes as `U,U_1,U_2,V`. The two initial Vieta polynomials are

\[
E_F(z,0)=(1+Uz^R)^2(1+Vz^d),
\tag{25}
\]

and

\[
E_G(z,0)=(1+U_1z^R)(1+U_2z^R)(1+Vz^d).
\tag{26}
\]

Their filler shell `d` is identical. At the terminal coefficient,

\[
(E_F)_N=U^2V,
\qquad
(E_G)_N=U_1U_2V.
\tag{27}
\]

If these differ, the limits of the terminal histories already differ because

\[
\lim_{s\to\infty}
\frac{(-1)^{N-1}P_N(s)}N
=E_N.
\tag{28}
\]

Suppose instead they are tuned to agree. Then

\[
U_1U_2=U^2.
\tag{29}
\]

All Vieta shells below `R` are common, while at shell `R`

\[
(E_F)_R=2U,
\qquad
(E_G)_R=U_1+U_2.
\tag{30}
\]

Because `U_1` and `U_2` are unit phases and the simple control requires `U_1!=U_2`, strict triangle inequality gives

\[
|U_1+U_2|<2=|2U|.
\tag{31}
\]

The relative tail `(22)` therefore forces

\[
\boxed{
P_N(F_N(s))\not\equiv P_N(G_N(s)).
}
\tag{32}
\]

So the asymptotically collision-saturated matched control of XF-125 cannot be upgraded to include the terminal harmonic history. The reason is not merely that `N=2R+d` lies in the additive semigroup. At degree `N`, Newton's logarithm couples complementary Vieta shells, and on a unit-circle slice that first complementary product becomes the noncancellable positive quantity `E_N|E_r|^2`.

This validates the boundary left explicitly open in XF-125: **proper-mode semigroup blindness and terminal-mode blindness are qualitatively different problems.**

## 4. What this does and does not recover about transition geometry

The result is positive but deliberately narrower than a collision criterion. A generic simple, irregular unit-circle divisor also has nonconstant `P_N(s)`. Therefore `(10)` does **not** say that one terminal history identifies a multiple root, nor does `(22)` exclude a more elaborate colliding/simple pair whose terminal histories agree while their Vieta shell magnitudes are arranged to match.

What is exact is the new information channel. Proper modes can be hidden by placing their complete trajectories outside an additive support semigroup. The terminal mode cannot be made identically blind in that way: its large-time tail scans the innermost active Vieta pair, and the first scan coefficient is positive after the self-inversive normalization. In this sense `P_N` is the first genuinely global scalar observable exposed by the periodic model.

For the Xi program the main obstruction is now source-side. The current exact source realization machinery of XF-118--XF-123 controls a prefix

\[
K=o(N),
\tag{33}
\]

whereas `P_N` lives exactly at full degree. XF-126 does not provide the actual Xi value or heat history of that terminal harmonic, and therefore does not by itself constrain the de Bruijn--Newman transition. It says instead that the negative results XF-124--XF-125 do **not** justify abandoning sparse/global observables altogether: a degree-scale aggregate can contain information that every sublinear family of proper coordinates misses.

The most useful next tests are consequently sharp. On the positive side, determine whether the Xi entire-function/periodization bridge exposes `P_N`, a controlled surrogate for its normalized heat tail, or another scalar aggregate of complementary Vieta shells at degree scale. On the adversarial side, ask whether there exist a colliding and an all-simple unit-circle divisor with the **same full terminal history** `P_N(s)` for all `s>=0`. A construction would show that even this global scalar is nonidentifying; a rigidity theorem would turn `(6)` into the first true one-observable collision detector in the periodic architecture.

## 5. Prior-art boundary

The external audit was aimed at three neighboring classes: self-inversive/unit-circle polynomial theory, Newton/power-sum reconstruction, and periodic polynomial backward heat flow. Classical self-inversive theory records the coefficient symmetry represented here by `(3)`, while Kabluchko's unitary-Hermite work treats periodic backward heat and unit-circle zero distributions in a broad asymptotic setting. Newton identities are of course classical. I did not find a source stating the specific terminal-harmonic heat-tail inversion `(6)`--`(9)`, the constant-history characterization `(10)`, or its use to separate the XF-125 collision/simple semigroup controls.

No external theorem is load-bearing for the new claim beyond literature already anchored in `SOURCES.md`: the proof is an exact consequence of XF-067's diagonal Vieta flow, the elementary unit-circle relation `(3)`, and the formal Newton logarithm `(11)`. `SOURCES.md` therefore needs no change.

## 6. Consequence for the current frontier

XF-124 and XF-125 establish a linear-information barrier for collections of individual **proper** harmonics. XF-126 identifies why that qualifier matters. The terminal coordinate is a nonlinear global compression of the whole Vieta state: its heat tail necessarily contains the first complementary-shell energy `|E_r|^2`.

The frontier is therefore no longer simply "add more high modes." It is to decide whether the actual Xi source can access even one such **degree-scale global observable**, or whether a stronger matched-control construction can also defeat terminal-history spectroscopy. Until one of those two tests is resolved, the terminal mode `m=N` is a live positive escape rather than another coordinate covered by the sparse-history obstruction.