# ANF-015 — Möbius oscillation strictly improves the Mellin lattice floor

**Status:** `EXACT-DERIVED + LITERATURE-OSCILLATION + DUAL-EXTREMAL-REDUCTION + STRUCTURAL-BOUNDARY`. The lattice-only lower bound

\[
c_*:=1+\frac{3}{\pi^2}
\]

from `ANF-014` is **provably not sharp** in the residual positive-spectral affine branch. The reason is not a numerical optimization accident. The all-scale periodization inequalities have a multiplicative packing dual, the `ANF-014` Mellin weight is one exactly saturated dual witness, and Möbius inversion describes every compactly supported first-order relaxation of that witness. The reduced cost of such a relaxation is precisely the centered weighted Möbius sum

\[
m_1(x):=\sum_{n\le x}\frac{\mu(n)}n-\frac{M(x)}x.
\]

Its Mellin transform is

\[
\int_1^\infty x m_1(x)x^{-s-1}\,dx
=\frac1{s(s-1)\zeta(s)}
\qquad(\Re s>1).
\]

Landau's oscillation principle, together with the nonreal zeros of `zeta`, forces `m_1` to take both signs arbitrarily far out. A negative interval gives an admissible perturbation of the Mellin dual witness with strictly larger objective. Consequently there exists a fixed `delta_lat>0` such that every normalized lattice-feasible profile satisfies

\[
\boxed{\frac{C(J)}{p(J)}\ge 1+\frac{3}{\pi^2}+\delta_{\rm lat}.}
\]

The argument is qualitative: it proves a strict gap but does not yet quantify `delta_lat`, so it does not close the remaining `0.0235357...` room up to Montgomery--Taylor.

## 1. Normalize the residual lattice problem

Retain the hypotheses and notation of `ANF-013`--`ANF-014`: `J` is continuous, real-even, nonnegative and supported in `[-1,1]`,

\[
P_J(h)=\frac1h\sum_{k\in\mathbb Z}J(k/h),
\qquad
p(J)=\inf_{h\ge1}P_J(h)>0,
\]

and

\[
C(J)=J(0)+2\int_0^1xJ(x)\,dx.
\]

Scale by `p(J)` and write again `J` for the normalized profile. Then

\[
P_J(h)\ge1\quad(h\ge1),
\qquad
J(0)=P_J(1)\ge1.
\tag{1}
\]

The scalar survival problem is therefore to lower-bound `C(J)` under the positive periodization constraints (1). Any such lower bound applies to `C(J)/p(J)` before normalization.

## 2. A multiplicative packing dual for all lattice constraints

Let `w:[1,\infty)\to[0,\infty)` be measurable and integrable enough for the expressions below, and define the multiplicative packing operator

\[
(Tw)(t):=\sum_{n\ge1}w(nt).
\tag{2}
\]

Assume

\[
\boxed{(Tw)(t)\le \frac1{t^2}\qquad(t\ge1).}
\tag{3}
\]

Since the `n=1` term is present, (3) gives `w(t)\le t^{-2}` and hence

\[
A_w:=\int_1^\infty\frac{w(h)}h\,dh\le\frac12.
\tag{4}
\]

Integrate the primal constraint `P_J(h)>=1` against `w`:

\[
I_w(J):=\int_1^\infty w(h)P_J(h)\,dh
\ge W_w:=\int_1^\infty w(h)\,dh.
\tag{5}
\]

Using evenness and nonnegativity, Tonelli plus the substitution `x=k/h` give

\[
\begin{aligned}
I_w(J)
&=J(0)A_w
+2\int_0^1\frac{J(x)}x
\sum_{k\ge1}w(k/x)\,dx\\
&=J(0)A_w
+2\int_0^1\frac{J(x)}x(Tw)(1/x)\,dx\\
&\le J(0)A_w+2\int_0^1xJ(x)\,dx.
\end{aligned}
\tag{6}
\]

Combining (4)--(6) with `J(0)>=1` yields the dual bound

\[
\boxed{
C(J)\ge D(w):=
1+\int_1^\infty w(h)\left(1-\frac1h\right)dh.
}
\tag{7}
\]

Thus every nonnegative packing weight satisfying (3) is a rigorous lower-bound certificate for the lattice-only extremal problem. No strong-duality assertion is needed for what follows.

## 3. The `ANF-014` Mellin floor is one saturated dual witness

Take

\[
w_0(t):=\frac{6}{\pi^2t^2}.
\tag{8}
\]

Then

\[
(Tw_0)(t)
=\frac{6}{\pi^2t^2}\sum_{n\ge1}\frac1{n^2}
=\frac1{t^2},
\tag{9}
\]

so every packing constraint is saturated. Its dual value is

\[
D(w_0)
=1+\frac6{\pi^2}\int_1^\infty
\left(\frac1{t^2}-\frac1{t^3}\right)dt
=1+\frac3{\pi^2}
=c_*.
\tag{10}
\]

Equation (10) recovers exactly the lower floor of `ANF-014`, but now as a dual certificate. This representation lets us ask whether the saturated witness itself has a feasible improving direction.

## 4. Möbius inversion gives all compactly supported slack directions

Let `g>=0` be bounded, nonzero and compactly supported in an interval of `(1,\infty)`. Define

\[
f(t):=-\sum_{n\ge1}\mu(n)g(nt).
\tag{11}
\]

For each `t>=1` this is a finite sum. Möbius inversion on the dilation semigroup gives

\[
\begin{aligned}
(Tf)(t)
&=-\sum_{k,n\ge1}\mu(n)g(nkt)\\
&=-\sum_{m\ge1}g(mt)\sum_{n\mid m}\mu(n)\\
&=-g(t).
\end{aligned}
\tag{12}
\]

Hence, for every `epsilon>0`,

\[
T(w_0+\epsilon f)(t)
=\frac1{t^2}-\epsilon g(t)
\le\frac1{t^2}.
\tag{13}
\]

Because `g` is compactly supported, `f` is bounded and supported in a compact subset of `[1,\infty)`. Since `w_0` has a positive minimum on that compact set, there exists `epsilon_0>0` such that

\[
w_\epsilon:=w_0+\epsilon f\ge0
\qquad(0<\epsilon\le\epsilon_0).
\tag{14}
\]

Thus (11) produces genuine feasible dual perturbations, not merely formal tangent directions.

Their objective is controlled by one arithmetic function. Put

\[
M(x):=\sum_{n\le x}\mu(n),
\qquad
m(x):=\sum_{n\le x}\frac{\mu(n)}n,
\qquad
R(x):=xm(x)-M(x)=xm_1(x).
\tag{15}
\]

Changing variables `u=nt` in (11) gives

\[
\boxed{
\int_1^\infty f(t)\left(1-\frac1t\right)dt
=-\int_1^\infty g(u)\frac{R(u)}u\,du.
}
\tag{16}
\]

Therefore

\[
\boxed{
D(w_\epsilon)-c_*
=-\epsilon\int_1^\infty g(u)\frac{R(u)}u\,du.
}
\tag{17}
\]

This identifies the exact reduced cost of relaxing the saturated Mellin witness: **negative mass of `R=xm_1` is an improving dual direction.**

## 5. The formal equality profile is exactly the centered Möbius sum

The Möbius boundary profile of `ANF-013`--`ANF-014` was

\[
G(x)=\frac12\left(
x\sum_{n\le x}\frac{\mu(n)}n-M(x)
\right).
\tag{18}
\]

Hence simply

\[
\boxed{G(x)=\frac{x}{2}m_1(x)=\frac12R(x).}
\tag{19}
\]

So the same arithmetic function has two exact roles:

- primal side: it is the unique formal profile that would make every normalized lattice periodization equal to its floor;
- dual side: its sign is the reduced cost of a Möbius-inverted relaxation of the all-scale packing witness.

This primal--dual identification is stronger than the appearance of Möbius inversion in `ANF-013` alone.

## 6. A Mellin transform forces `R` to oscillate in sign

There is also an exact transform identity. From (15),

\[
R(x)=\sum_{n\le x}\mu(n)\left(\frac{x}{n}-1\right).
\tag{20}
\]

For `Re(s)>1`, absolute convergence permits termwise integration:

\[
\begin{aligned}
\int_1^\infty R(x)x^{-s-1}\,dx
&=\sum_{n\ge1}\mu(n)
\int_n^\infty\left(\frac{x}{n}-1\right)x^{-s-1}\,dx\\
&=\frac1{s(s-1)}\sum_{n\ge1}\frac{\mu(n)}{n^s}.
\end{aligned}
\]

Therefore

\[
\boxed{
\int_1^\infty R(x)x^{-s-1}\,dx
=\frac1{s(s-1)\zeta(s)}.
}
\tag{21}
\]

Now apply Landau's classical oscillation principle in Mellin/Laplace form. If `R` were eventually nonnegative, the Mellin transform of a sufficiently far tail would have a singularity at its real abscissa of convergence. Subtracting the compact initial segment changes (21) only by an entire function.

But the meromorphic continuation on the right side of (21) has **no positive-real singularity**: `s=1` is removable because the pole of `zeta` cancels `s-1`; for `0<s<1`, `zeta(s)` is nonzero (for example from the alternating eta representation); and for `s>1` the Euler product is nonzero. On the other hand, every nontrivial zero `rho` of `zeta` gives a nonreal pole of (21) with `0<Re(rho)<1`. Therefore the abscissa cannot be positive real, while if it were nonpositive the tail transform would be analytic throughout `Re(s)>0`, contradicting those nonreal poles.

Thus `R` cannot be eventually nonnegative. Applying the same argument to `-R` shows that it cannot be eventually nonpositive either. Consequently

\[
\boxed{R(x)\text{ takes both positive and negative values arbitrarily far out}.}
\tag{22}
\]

Since `R` is continuous — a newly entering term in (20) vanishes at its entry point — every strict sign occurrence contains a nontrivial interval of that sign.

## 7. The lattice-only floor is strictly above `1+3/pi^2`

Choose a compact interval `I` on which `R<0`, and choose any bounded nonzero `g>=0` supported inside `I`. Then (17) gives

\[
D(w_\epsilon)-c_*
=-\epsilon\int_I g(u)\frac{R(u)}u\,du
>0
\tag{23}
\]

for every sufficiently small positive `epsilon` allowed by (14). By the dual lemma (7), this one fixed witness bounds **every** normalized lattice-feasible profile. Hence there is a constant

\[
\delta_{\rm lat}:=D(w_\epsilon)-c_*>0
\]

such that

\[
\boxed{
C(J)\ge1+\frac3{\pi^2}+\delta_{\rm lat}
}
\tag{24}
\]

for all normalized profiles satisfying the full lattice-periodization constraints. Undoing the normalization gives

\[
\boxed{
\frac{C(J)}{p(J)}
\ge1+\frac3{\pi^2}+\delta_{\rm lat}.
}
\tag{25}
\]

In particular, the equality boundary of `ANF-014` is not admissible in the nonnegative spectral class: by (19) and (22), its formal profile changes sign. More strongly, (24) supplies a uniform strict separation from that boundary rather than merely proving non-attainment.

The theorem is deliberately **non-quantitative**. Landau oscillation proves the existence of a negative interval, and compact support then gives some admissible `epsilon`, but the argument does not estimate the resulting `delta_lat`. It therefore shrinks the `Delta_MT=0.0235357453...` budget from `ANF-014` by an unknown positive amount; it does not establish that the remaining budget is exhausted.

## 8. Prior art and novelty boundary

The weighted Möbius sums `M(x)` and `m(x)=sum_{n<=x}mu(n)/n`, Möbius inversion, the Dirichlet series `1/zeta(s)`, and Landau-type oscillation arguments are classical analytic number theory. Bateman--Diamond's *Analytic Number Theory: An Introductory Course* treats Landau's oscillation theorem as a standard tool, and Johnston--Trudgian's 2026 survey/article gives a current account of the Landau--Pintz mechanism with the Möbius function as a prototype. Modern work on explicit conversions and estimates for Möbius summatory functions likewise confirms that `m` and its centered variants are established arithmetic objects.

A targeted search across periodization extremal problems, multiplicative packing inequalities, Möbius summatory identities and Landau oscillation did not locate the specific dual certificate (7), the Möbius slack formula (11)--(17), or the conclusion that zeta-zero-driven sign oscillation forces a strict improvement over the `ANF-014` lattice floor in this simple-critical-zero certificate problem. No publication-level novelty claim is made. The durable contribution is the **primal--dual bridge**: the formal Möbius saturation profile is simultaneously the reduced-cost obstruction to sharpness of the Mellin lattice witness.

## 9. Consequence and decisive next test

`ANF-014` left open whether its lower floor might itself be sharp. That possibility is now closed. The scalar branch must pay a strictly positive arithmetic stability cost above `1+3/pi^2` before the full complex-configuration inequalities are even considered.

The next question is quantitative rather than qualitative. One route is to turn an explicit negative interval for `m_1` into an explicit admissible packing perturbation and optimize its dual gain. A stronger route is to optimize the full multiplicative packing dual (3) and ask whether its value reaches

\[
C_{\rm MT}=1.3274992963\ldots .
\]

Reaching `C_MT` would close the entire thermodynamic-lattice survival stage of the universal affine scalar route. Falling strictly below it would still leave the second-stage universal complex-configuration inequality unresolved. The configuration-level escape of `ANF-006` remains outside this obstruction.