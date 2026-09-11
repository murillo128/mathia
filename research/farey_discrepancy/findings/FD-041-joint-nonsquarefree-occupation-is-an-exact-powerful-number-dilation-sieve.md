# FD-041 — joint nonsquarefree occupation is an exact powerful-number dilation sieve

**Status:** `EXACT-DERIVED + JOINT-NONSQUAREFREE-OCCUPATION + DIRICHLET-CONVOLUTION + POWERFUL-NUMBER-SIEVE + MULTISCALE-ENERGY + SCALING-BOUNDARY`.

`FD-035` shows that treating the prime-square row families separately cannot force a pointwise projective gap, while `FD-037`--`FD-040` progressively restrict the ways in which the physical quotient-shell source could evade the full nonsquarefree union. The remaining joint-occupation clue therefore asks whether keeping all overlaps before lower-bounding retains information that the separate square recurrences discard.

For the **untruncated** Jordan energy, that overlap can be eliminated exactly. The full squarefree-row energy is a Dirichlet-convolution transform of the total energy, and the quotient kernel is supported only on powerful numbers. Equivalently, the full nonsquarefree occupation is an exact signed dilation sieve of the single scalar total-energy curve.

This gives two durable consequences. First, there is no hidden independent overlap datum in the untruncated union: once the scalar energy is known at all smaller horizons, the nonsquarefree energy is already determined exactly. Second, any total-energy profile with a dominated multiplicative scaling law of index `alpha>1/2` has an explicit strictly positive asymptotic nonsquarefree fraction. At `alpha=1` that fraction is exactly the constant `delta_ns=0.3558...` found independently from terminal quotient blocks in `FD-038`.

For the physical half-linear regime this is directly relevant because `D=1`, and rows `1,2,3` are all squarefree. Thus a vanishing nonsquarefree fraction for `D<=3` would force the **untruncated scalar energy itself** to violate every such regular multiplicative scaling law. Combined with `FD-040`, a physical escape in the half-linear regime must therefore involve both genuinely growing/infinite spectral complexity and genuinely multiplicatively irregular energy growth; finite-packet coercivity and scalar regular scaling are two independent ways to rule it out.

## 1. Hyperbola operators compose by Dirichlet convolution

Let `F:N->R` be any shell profile and put

\[
f(n):=F(n)^2.
\tag{1}
\]

For an arithmetic function `a`, define the floor-hyperbola operator

\[
(\mathcal T_a f)(H)
:=
\sum_{r\le H}a(r)
 f\!\left(\left\lfloor\frac Hr\right\rfloor\right).
\tag{2}
\]

For arbitrary arithmetic functions `a,b`, the elementary floor identity

\[
\left\lfloor
\frac{\lfloor H/d\rfloor}{e}
\right\rfloor
=
\left\lfloor\frac{H}{de}\right\rfloor
\tag{3}
\]

gives the exact composition law

\[
\boxed{
\mathcal T_a\mathcal T_b
=
\mathcal T_{a*b},
}
\tag{4}
\]

where `*` denotes Dirichlet convolution. Indeed,

\[
\begin{aligned}
(\mathcal T_a\mathcal T_b f)(H)
&=\sum_{d\le H}a(d)
  \sum_{e\le H/d}b(e)
  f\!\left(\left\lfloor\frac{H}{de}\right\rfloor\right)\\
&=\sum_{n\le H}(a*b)(n)
  f\!\left(\left\lfloor\frac Hn\right\rfloor\right).
\end{aligned}
\tag{5}
\]

No asymptotics or source property enters this identity.

Now use the Jordan weight from `FD-033`--`FD-040`,

\[
w(r):=\frac{J_2(r)}{r^2}
=\prod_{p\mid r}(1-p^{-2}),
\tag{6}
\]

and its squarefree restriction

\[
s(r):=\mu(r)^2w(r).
\tag{7}
\]

Define the untruncated total, squarefree, and nonsquarefree energies

\[
\mathscr E_H^F:=\mathcal T_w f(H),
\qquad
\mathscr S_H^F:=\mathcal T_s f(H),
\qquad
\mathscr U_H^F:=\mathscr E_H^F-\mathscr S_H^F.
\tag{8}
\]

Since `w(1)=1`, the arithmetic function `w` has a Dirichlet inverse. Put

\[
q:=s*w^{-1}.
\tag{9}
\]

Then `s=q*w`, so (4) immediately gives

\[
\boxed{
\mathscr S_H^F
=
\mathcal T_q\mathscr E^F(H)
=
\sum_{d\le H}q(d)
\mathscr E_{\lfloor H/d\rfloor}^F.
}
\tag{10}
\]

Thus the squarefree/nonsquarefree row split is already encoded in the scalar curve `H -> mathscr E_H^F`.

## 2. The quotient kernel is supported exactly on powerful numbers

The local Dirichlet series are especially simple. For a prime `p`, set

\[
a_p:=1-p^{-2}.
\tag{11}
\]

Because `w(p^k)=a_p` for every `k>=1`, while `s(p)=a_p` and `s(p^k)=0` for `k>=2`, their local generating functions in a formal variable `z` are

\[
W_p(z)
=1+a_p(z+z^2+\cdots)
=\frac{1-p^{-2}z}{1-z},
\tag{12}
\]

\[
S_p(z)=1+a_pz.
\tag{13}
\]

Hence

\[
Q_p(z)
:=\frac{S_p(z)}{W_p(z)}
=
1-
\frac{a_pz^2}{1-p^{-2}z}.
\tag{14}
\]

Comparing coefficients yields

\[
\boxed{
q(1)=1,
\qquad
q(p)=0,
\qquad
q(p^k)=-(1-p^{-2})p^{-2(k-2)}
\quad(k\ge2).
}
\tag{15}
\]

Since `q` is multiplicative, `q(n)=0` whenever some prime divides `n` to exponent exactly one. Therefore its nontrivial support consists exactly of **powerful numbers**: integers in which every occurring prime has exponent at least two.

For a powerful integer

\[
d=\prod_p p^{e_p},
\qquad e_p\in\{0\}\cup[2,\infty),
\tag{16}
\]

one has explicitly

\[
q(d)
=(-1)^{\omega(d)}
\prod_{p\mid d}
(1-p^{-2})p^{-2(e_p-2)}.
\tag{17}
\]

As `q(1)=1`, equation (10) becomes the exact joint nonsquarefree identity

\[
\boxed{
\mathscr U_H^F
=
-\sum_{\substack{2\le d\le H\\d\ \mathrm{powerful}}}
q(d)\,
\mathscr E_{\lfloor H/d\rfloor}^F.
}
\tag{18}
\]

The first layer `d=p^2` has positive coefficient after the leading minus sign:

\[
-q(p^2)=1-p^{-2}.
\tag{19}
\]

The next mixed layer `d=p^2q^2` has negative coefficient, and so on. Thus (18) is precisely the overlap-corrected inclusion-exclusion that the accepted joint-occupation clue asks for. The separate prime-square inequality of `FD-034` is recovered by retaining one positive row family and discarding the rest before inclusion-exclusion; (18) shows what was lost by that operation.

## 3. Dominated multiplicative scaling forces a positive occupation constant

The powerful kernel is sparse enough that its Mellin transform is absolutely summable well below the linear exponent. For every `alpha>1/2`,

\[
\begin{aligned}
\sum_{d\ge1}\frac{|q(d)|}{d^\alpha}
&=\prod_p
\left(
1+
\frac{(1-p^{-2})p^{-2\alpha}}
     {1-p^{-(\alpha+2)}}
\right)\\
&<\infty,
\end{aligned}
\tag{20}
\]

because the logarithm of the Euler product is `O(sum_p p^(-2 alpha))`.

Suppose now that a positive scalar energy curve `mathscr E_H` satisfies the following **dominated multiplicative scaling law** for some `alpha>1/2`. For every fixed positive integer `d`,

\[
\frac{\mathscr E_{\lfloor H/d\rfloor}}
     {\mathscr E_H}
\longrightarrow d^{-\alpha},
\tag{21}
\]

and there exist `epsilon` and `C` with

\[
0<\epsilon<\alpha-\frac12
\tag{22}
\]

such that, for all sufficiently large `H` and every `1<=d<=H`,

\[
\frac{\mathscr E_{\lfloor H/d\rfloor}}
     {\mathscr E_H}
\le C d^{-\alpha+\epsilon}.
\tag{23}
\]

The hypothesis is deliberately stated in the exact form needed here; no external regular-variation theorem is imported. Ordinary power and power-log profiles with the corresponding two-sided asymptotic bounds satisfy it.

Equations (20)--(23) permit dominated convergence directly in (10). Therefore

\[
\boxed{
\frac{\mathscr S_H}{\mathscr E_H}
\longrightarrow
Q(\alpha)
:=\sum_{d\ge1}\frac{q(d)}{d^\alpha}
}
\tag{24}
\]

and

\[
\boxed{
\frac{\mathscr U_H}{\mathscr E_H}
\longrightarrow
\delta_{\mathrm{pow}}(\alpha)
:=1-Q(\alpha)>0.
}
\tag{25}
\]

The Euler product is

\[
\boxed{
Q(\alpha)
=
\prod_p
\frac{
(1+(1-p^{-2})p^{-\alpha})(1-p^{-\alpha})
}{1-p^{-(\alpha+2)}}.
}
\tag{26}
\]

Every local factor lies strictly between zero and one, and its deficit from one is `asymp p^(-2 alpha)`. Since `2 alpha>1`, the product converges to a strictly positive number smaller than one, proving the final inequality in (25).

This is stronger than merely observing that one fixed prime-square scale survives. It gives the exact asymptotic occupation produced by the **entire overlapping nonsquarefree union**, with every multiple-square correction already included.

## 4. The `FD-038` density constant is exactly the linear-scaling member

At `alpha=1`, the local factor in (26) simplifies to

\[
\frac{
(1+(1-p^{-2})p^{-1})(1-p^{-1})
}{1-p^{-3}}
=
\frac{1-p^{-2}-p^{-3}+p^{-4}}
     {1-p^{-3}}.
\tag{27}
\]

Consequently

\[
Q(1)
=
\zeta(3)
\prod_p(1-p^{-2}-p^{-3}+p^{-4}).
\tag{28}
\]

The product on the right is exactly the weighted squarefree density `c_sf` from `FD-038`. Hence

\[
\boxed{
\delta_{\mathrm{pow}}(1)
=1-\zeta(3)c_{\mathrm{sf}}
=\delta_{\mathrm{ns}}
=0.3558\ldots .
}
\tag{29}
\]

This agreement is an independent consistency check on both calculations. `FD-038` obtains the same constant locally from long quotient blocks, without any global scaling hypothesis. The present identity explains why that constant is also the fixed occupation ratio of the exact powerful-number sieve when the total scalar energy scales linearly across multiplicative dilations.

The mechanisms are therefore complementary. `FD-038` is unconditional on a terminal bulk but does not control sparse low-row amplification; `FD-041` controls the full row union whenever the **scalar energy curve itself** has stable multiplicative scaling.

## 5. Consequence for the physical half-linear frontier

Return to the physical shell profile

\[
F(n)=\mathcal H(n)
\tag{30}
\]

from `FD-033`, and write `mathscr E_H=E_(H,0)` and `mathscr U_H=U_(H,0)` for the untruncated energies. For `D=1,2,3`, every deleted Jordan row is squarefree. Therefore

\[
\boxed{
U_{H,D}=\mathscr U_H
\qquad(D\le3),
}
\tag{31}
\]

while

\[
E_{H,D}\le\mathscr E_H.
\tag{32}
\]

If the full physical energy obeys (21)--(23) for some `alpha>1/2`, equations (25), (31), and (32) give

\[
\boxed{
\liminf_{H\to\infty}
\frac{U_{H,D}}{E_{H,D}}
\ge
\delta_{\mathrm{pow}}(\alpha)>0
\qquad(D=1,2,3).
}
\tag{33}
\]

In particular, `D=1` is the Schur head arising from the half-linear prime-prefix regime. Thus a half-linear vanishing-occupation sequence cannot coexist with any dominated multiplicative scaling law for the untruncated physical energy.

Equivalently, if for some `D<=3` an unbounded sequence `H_j` satisfied

\[
\frac{U_{H_j,D}}{E_{H_j,D}}\longrightarrow0,
\tag{34}
\]

then also

\[
\frac{\mathscr U_{H_j}}{\mathscr E_{H_j}}\longrightarrow0,
\tag{35}
\]

and the scalar curve `mathscr E` must fail (21)--(23) along that sequence. This makes the remaining escape more specific than the sparse-spike control of `FD-039`: the physical source would have to create multiplicatively unstable scalar energy, not merely complicated rowwise phases.

This does **not** prove that the physical energy satisfies (21)--(23). Nor does it settle the accepted occupation clue for arbitrary fixed `D`: once `D>=4`, the deleted head already contains nonsquarefree rows and the clean convolution factorization (31) no longer transfers the full-union ratio directly to the Schur tail. The truncation boundary is genuine and is not hidden in the notation.

## 6. Relation to `FD-040`, prior art, and falsification boundary

`FD-040` and the present result constrain different failure modes. `FD-040` proves coercivity for a finite supercritical Mellin packet even when its phase makes the scalar energy oscillatory. `FD-041` permits arbitrarily complicated shell profiles, including potentially infinite spectral content, but requires the **quadratic total energy** to settle to a dominated multiplicative scaling law. Therefore a physical half-linear escape that survives both findings must simultaneously exploit spectral complexity beyond every fixed packet and energy growth irregular enough to defeat stable dilation ratios.

Dirichlet convolution, multiplicative inverses, Jordan totients, squarefree indicators, and powerful numbers are classical objects. A targeted prior-art audit around squarefree/powerful Dirichlet inverses, Jordan-totient Dirichlet series, and floor-hyperbola convolution operators found standard versions of those ingredients but no external theorem needed for (4), (15), or (18). No novelty is claimed for the algebraic concepts in isolation. The Mathia-specific contribution is their exact placement in the joint Jordan-row occupation problem, the powerful-kernel identity (18), and the bridge (29) to the independently derived `FD-038` density constant. No new `SOURCES.md` dependency is load-bearing.

The finding is falsified if the floor composition (4) fails, if the local quotient (14) does not produce (15), or if direct finite evaluation of an arbitrary shell profile violates (10) or (18). The scaling consequence is falsified if a curve satisfying the explicit hypotheses (21)--(23) does not converge to the Euler-product ratio (24)--(26). It must not be cited as proof that the physical energy is regularly varying, as a pointwise occupation theorem for `D>=4`, or as an RH proof.

The next source-specific target is now sharper: either prove enough multiplicative regularity for the physical scalar energy to invoke (25), or explain arithmetically how the exact coefficient law `Delta mathcal H(n)=mu(rad n)phi(rad n)/n` can generate the dilation instability required by (34)--(35). Merely adding more separate prime-square recurrences, or merely observing the overlaps of their union, no longer constitutes a distinct route.