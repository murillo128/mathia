# AF-395 — Fixed-radius prime stencils cannot recover PF3 curvature topology

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `PF3` · `PRIME-LOGS` · `LOCAL-TO-GLOBAL` · `BOUNDARY-TOPOLOGY` · `NEGATIVE/OBSTRUCTION` · `NO-NOVELTY-CLAIM`

## Claim

AF-382 shows that at order two, eventual nearest-neighbor prime-ratio minors already determine global translation `TN_2`. That locality phenomenon fails sharply at order three.

Let

\[
e_1<e_2<\cdots,\qquad e_n\to\infty,
\]

be any increasing sampling sequence whose tail mesh

\[
\delta_N:=\sup_{n\ge N}(e_{n+1}-e_n)
\tag{1}
\]

satisfies

\[
\delta_N\longrightarrow0.
\tag{2}
\]

There exists a strictly positive `C^\infty` integrable profile

\[
f:\mathbb R\to(0,\infty)
\tag{3}
\]

such that all three statements hold:

1. the translation kernel
   \[
   K_f(u,x)=f(u-x)
   \]
   is globally `TN_2`;
2. `K_f` is **not** `TN_3`;
3. for every fixed index radius `R`, there is `N_R` such that every sampled order-three minor with
   \[
   N_R\le i_1<i_2<i_3,\qquad i_3-i_1\le R,
   \]
   and
   \[
   N_R\le j_1<j_2<j_3,\qquad j_3-j_1\le R
   \]
   is nonnegative:
   \[
   \det\bigl(f(e_{i_a}-e_{j_b})\bigr)_{a,b=1}^3\ge0.
   \tag{4}
   \]

Thus **no fixed-radius local stencil family on a vanishing-mesh sampling sequence is target-faithful for smooth `TN_3`**, even when full order-two total nonnegativity is supplied independently.

The failure is quantitative. For the profile constructed below, every negative sampled order-three minor using tail indices at least `N` must satisfy

\[
(i_3-i_1)+(j_3-j_1)>\frac{2}{\delta_N},
\tag{5}
\]

and therefore

\[
\max\{i_3-i_1,j_3-j_1\}>\frac1{\delta_N}.
\tag{6}
\]

Nevertheless negative sampled minors exist in every sufficiently far tail. Hence the missing resource is not sampling density but **nonlocal combinatorial reach**: as the physical mesh shrinks, a witness to the global curvature-component obstruction must span more and more sample indices.

For rational primes,

\[
e_n=\log p_n,
\tag{7}
\]

condition `(2)` follows from the prime number theorem. Consequently every fixed successor-prime stencil, including every fully adjacent `3\times3` prime-ratio minor, is eventually nonnegative for this `f`, while the full prime-ratio family still contains negative `3\times3` minors arbitrarily far out.

Using the Baker--Harman--Pintz gap bound already audited in AF-380/AF-381 gives the optional quantitative specialization

\[
\delta_N=O\!\left(p_N^{-19/40}\right),
\tag{8}
\]

so any negative tail prime-ratio witness for this profile must have at least one row or column index span

\[
\Omega\!\left(p_N^{19/40}\right).
\tag{9}
\]

The exponent is not the conceptual point. The robust conclusion is that **bounded successor depth cannot carry the component topology isolated by AF-394**.

## Explicit smooth profile

Define the standard flat bump

\[
\beta(s)=
\begin{cases}
\exp\!\left(-\dfrac1{1-s^2}\right),&|s|<1,\\[1ex]
0,&|s|\ge1,
\end{cases}
\tag{10}
\]

and the two-component logarithmic curvature

\[
q(t)=\beta(t+2)+\beta(t-2).
\tag{11}
\]

Then

\[
\Omega:=\{q>0\}=(-3,-1)\cup(1,3),
\tag{12}
\]

so the two positive-curvature components are separated by the zero interval `[-1,1]` of length two.

Set

\[
g(t)=-\int_0^t (t-s)q(s)\,ds,
\qquad
f(t)=e^{g(t)}.
\tag{13}
\]

Then

\[
g''=-q,
\qquad
-(\log f)''=q\ge0.
\tag{14}
\]

Thus `g=\log f` is concave and `K_f\in TN_2` by the classical `PF_2` / log-concavity criterion used in AF-382.

The function is also integrable. Because `q` is even and compactly supported, `g'` is a positive constant on the far left and the opposite negative constant on the far right, so `g(t)\to-\infty` linearly at both ends.

Inside either component, writing `s=t\mp2`,

\[
\log q(t)=-\frac1{1-s^2}
\]

and direct differentiation gives

\[
(\log q)''(t)
=-\frac{2(1+3s^2)}{(1-s^2)^3}<0.
\tag{15}
\]

In particular

\[
(\log q)''\le2q
\tag{16}
\]

on each positive component. So the profile satisfies every local analytic condition in AF-394; the only failed `TN_3` condition is connectedness of `\{q>0\}`.

## An explicit global negative minor

The failure of `TN_3` can be seen without appealing only to the abstract classification.

Take column gaps

\[
a=\frac12,
\qquad
b=1,
\]

and define, as in AF-394,

\[
U(t)=\frac{f(t-a)}{f(t)},
\qquad
V(t)=\frac{f(t-a-b)}{f(t)}.
\tag{17}
\]

Their logarithmic derivatives are

\[
(\log U)'(t)=A(t):=\int_{t-1/2}^{t}q(s)\,ds,
\tag{18}
\]

and

\[
(\log V)'(t)=A(t)+B(t),
\qquad
B(t):=\int_{t-3/2}^{t-1/2}q(s)\,ds.
\tag{19}
\]

For every `t\in[0,1/4]`, the `A`-window lies inside the zero gap, so

\[
A(t)=0,
\tag{20}
\]

while the `B`-window overlaps the left bump, so

\[
B(t)>0.
\tag{21}
\]

Hence

\[
U(0)=U(1/4),
\qquad
V(0)<V(1/4).
\tag{22}
\]

By `t=3/2`, the `A`-window has entered the right bump, giving

\[
U(3/2)>U(1/4).
\tag{23}
\]

Therefore the normalized determinant with rows

\[
t_1=0,\qquad t_2=\frac14,\qquad t_3=\frac32
\tag{24}
\]

and columns

\[
x_1=0,\qquad x_2=\frac12,\qquad x_3=\frac32
\tag{25}
\]

has sign

\[
\det
\begin{pmatrix}
1&U(t_1)&V(t_1)\\
1&U(t_2)&V(t_2)\\
1&U(t_3)&V(t_3)
\end{pmatrix}
=-(U(t_3)-U(t_1))(V(t_2)-V(t_1))<0.
\tag{26}
\]

Row normalization divides the original translation matrix by positive factors `f(t_i)`, so the corresponding raw `3\times3` translation minor is also strictly negative. Thus

\[
K_f\notin TN_3.
\tag{27}
\]

This is exactly the positive-curvature component obstruction isolated abstractly in AF-394.

## Locality lemma: a short argument window sees at most one component

Let

\[
u_1<u_2<u_3,
\qquad
x_1<x_2<x_3,
\]

and let the complete interval of arguments used by the minor be

\[
I=[u_1-x_3,\,u_3-x_1].
\tag{28}
\]

Its length is

\[
|I|=(u_3-u_1)+(x_3-x_1).
\tag{29}
\]

Suppose

\[
|I|<2.
\tag{30}
\]

Since the two components in `(12)` are separated by distance two, `I` cannot meet both of them.

If `I` meets only the right component, let

\[
q_*(t)=\beta(t-2).
\]

If it meets only the left component, let

\[
q_*(t)=\beta(t+2).
\]

If it meets neither component, take `q_*\equiv0`. In every case,

\[
q_*=q\quad\text{on }I.
\tag{31}
\]

Choose any smooth `g_*` satisfying

\[
g_*''=-q_*,
\qquad
f_*=e^{g_*}.
\tag{32}
\]

The positive set of `q_*` is an interval (or empty), and `(15)` gives the AF-394 differential condition on it. Hence

\[
K_{f_*}\in TN_3.
\tag{33}
\]

On `I`, equations `(14)`, `(31)`, and `(32)` give

\[
(g-g_*)''=0,
\]

so for constants `\alpha,\gamma`,

\[
g(t)-g_*(t)=\alpha t+\gamma
\qquad(t\in I).
\tag{34}
\]

Every entry of the original minor therefore factors as

\[
f(u_a-x_b)
=e^\gamma e^{\alpha u_a}e^{-\alpha x_b}
 f_*(u_a-x_b).
\tag{35}
\]

The row and column factors in `(35)` are positive. They cannot change the determinant sign. By `(33)`, the determinant is nonnegative.

Thus we have the exact local statement

\[
\boxed{
(u_3-u_1)+(x_3-x_1)<2
\quad\Longrightarrow\quad
\det(f(u_a-x_b))_{a,b=1}^3\ge0.
}
\tag{36}
\]

The global negative sign is therefore invisible to every order-three observation whose full argument hull is shorter than the zero gap separating the two curvature components.

## Vanishing mesh makes every fixed-radius stencil eventually blind

Take sampled rows and columns from the tail, with

\[
i_3-i_1\le R,
\qquad
j_3-j_1\le R.
\tag{37}
\]

By definition of `\delta_N`,

\[
e_{i_3}-e_{i_1}\le R\delta_N,
\qquad
 e_{j_3}-e_{j_1}\le R\delta_N.
\tag{38}
\]

Hence the sampled argument interval has length at most

\[
2R\delta_N.
\tag{39}
\]

For each fixed `R`, choose `N_R` so large that

\[
R\delta_{N_R}<1.
\tag{40}
\]

Then `(39)` is strictly below two, and the locality lemma `(36)` proves every local sampled order-three minor `(4)` nonnegative.

This proves more than failure of the literal adjacent `3\times3` test. Enlarging the successor stencil to any **fixed** number of neighboring samples does not repair target fidelity. The same profile defeats every fixed radius; only the tail threshold changes with `R`.

## Every negative tail witness must become index-nonlocal

Conversely, suppose a sampled tail minor is negative. By `(36)`, its argument interval must have length at least two. Therefore

\[
(e_{i_3}-e_{i_1})+(e_{j_3}-e_{j_1})>2.
\tag{41}
\]

Using `(1)`,

\[
(e_{i_3}-e_{i_1})+(e_{j_3}-e_{j_1})
\le
\bigl((i_3-i_1)+(j_3-j_1)\bigr)\delta_N.
\tag{42}
\]

Combining `(41)` and `(42)` gives `(5)` and `(6)`.

At the same time, negative sampled minors do not disappear. The explicit continuum minor `(26)` has a fixed negative margin. Translate all six row/column coordinates by a common large `T`. Because the tail mesh tends to zero, sampled points can approximate the translated row and column configurations simultaneously and arbitrarily well. Translation cancels in all differences, and determinant continuity preserves the strict negative sign. Thus every sufficiently far tail contains a negative sampled `3\times3` minor.

The two facts coexist:

\[
\text{full sampled family detects the defect},
\qquad
\text{every fixed-radius sampled family eventually misses it}.
\tag{43}
\]

This is a concrete information-loss statement, not merely a warning that there are many minors to check.

## Prime-log specialization

For

\[
e_n=\log p_n,
\tag{44}
\]

the prime number theorem implies

\[
e_{n+1}-e_n=\log\frac{p_{n+1}}{p_n}\to0.
\tag{45}
\]

So the theorem applies directly. In particular, for sufficiently large `i,j`,

\[
\det\left(
 f\!\left(\log\frac{p_{i+a}}{p_{j+b}}\right)
\right)_{a,b=0}^{2}\ge0,
\tag{46}
\]

even though `K_f\notin TN_3` and full prime-ratio sampling contains negative order-three minors in every far tail.

AF-381 already records the Baker--Harman--Pintz estimate in the form

\[
\log\frac{p_{n+1}}{p_n}
=O\!\left(p_n^{-19/40}\right).
\tag{47}
\]

Since `p_n\ge p_N` for `n\ge N`, equation `(47)` gives `(8)`. Substitution into `(6)` yields `(9)`: the index reach of a negative witness grows at least polynomially along the prime tail.

This lower bound concerns **combinatorial reach in the ordered prime sequence**, not determinant order. The determinant order remains three throughout. What diverges is how far apart the retained prime labels must be allowed to interact.

## Fidelity interpretation

AF-382 found an exact order-two locality miracle: positivity lets logarithms convert adjacent `2\times2` inequalities into additive mixed differences, and those local generators telescope to every rectangle.

AF-395 shows why there is no analogous unrestricted order-three conclusion from bounded successor depth. The obstruction in AF-394 is a component relation. Shrinking physical mesh makes every fixed index neighborhood more local, so it eventually sees at most one curvature component. Inside one component the profile is genuinely `TN_3`; the failure exists only in the ordering relation **between** components.

This separates three resources that can otherwise be conflated:

- **resolution:** `\delta_N\to0` gives arbitrarily accurate local sampling;
- **determinant arity:** order three is already sufficient to witness the failure;
- **relational reach:** the rows/columns must connect locations separated by the global curvature gap.

More resolution does not compensate for bounded reach. In fact it makes a fixed successor stencil physically narrower, forcing the necessary index span to diverge.

The result also sharpens AF-383. Row-consecutive Toeplitz generators remain target-complete because they retain **arbitrary columns**. The present counterexample shows why replacing that unbounded placement freedom by a fixed-radius two-axis stencil can lose the target even for smooth positive profiles at order three.

## Riemann-facing consequence

For an RH-facing Pólya-frequency route, proving eventual positivity of successor-prime `3\times3` minors, or of any fixed finite neighborhood of prime indices, cannot by itself settle the order-three layer on an unrestricted smooth source class.

A successful source-side argument must provide at least one additional resource:

- nonlocal prime interactions whose index reach grows with the sampling scale;
- an independent theorem forcing the relevant positive-curvature set to be connected;
- or a stronger source rigidity statement that rules out the two-component fibre represented by `(11)`.

This is not evidence that the actual Riemann profile has disconnected curvature or that local prime inequalities are useless. The counterexample is a target-fidelity obstruction: **bounded local prime stencils do not retain enough information to distinguish the global `PF_3` target without extra source structure**.

That distinction matters because the prime symbols in `(46)` are not themselves the missing arithmetic discriminator. A nonarithmetic vanishing-mesh sequence has the identical blind spot. Prime specificity would have to enter through a theorem that forces the missing global resource, not through the local sampling geometry alone.

## Prior art and novelty audit

The surrounding ingredients are classical or already audited locally, and no novelty claim is made.

- H. F. Weinberger, **“A Characterization of the Polya Frequency Functions of Order 3,”** *Applicable Analysis* **15**(1--4) (1983), 53--69, DOI `10.1080/00036818308839439`. Role: classical `PF_3` characterization territory. AF-394 already treats the smooth curvature-support characterization as literature-adjacent rather than novel.
- Michael I. Ganzburg, **“On E-Pólya Frequency Functions,”** *Journal of Mathematical Analysis and Applications* **346**(1) (2008), 1--8, DOI `10.1016/j.jmaa.2008.04.070`. Role: established determining-set theory for translation total positivity when sufficiently rich sampled information is retained. The present obstruction concerns the much stronger compression to bounded local stencils on both sampled axes, so it does not conflict with `E`-Pólya-frequency determination.
- Christian Grussler and Tobias Damm, **“Efficient k-Sign Consistency Verification of Hankel Matrices via Schur Polynomials,”** arXiv:`2602.08122` (2026). Role: current structured-minor recognition showing that fixed-order Hankel/Toeplitz sign consistency can be reduced to row-consecutive generators while retaining arbitrary opposite-axis placements. AF-383 already imports that mechanism; AF-395 identifies an explicit smooth reason bounded two-axis locality can lose information.
- R. C. Baker, G. Harman, and J. Pintz, **“The Difference Between Consecutive Primes, II,”** *Proceedings of the London Mathematical Society* **83**(3) (2001), 532--562, DOI `10.1112/plms/83.3.532`. Role: quantitative prime-gap input for `(47)` and therefore for the optional index-reach rate `(9)`; this source is already audited in AF-380/AF-381.

A focused search for order-three Pólya-frequency recognition from bounded local/consecutive stencils, including prime-sampled variants, did not identify this exact smooth two-bump obstruction. That absence is not evidence of novelty. The durable Arithmetic Fidelity contribution is the resource theorem: **a global component discriminator can survive at determinant order three while escaping every fixed-radius observation on an increasingly fine sampling grid**.

## Boundaries and falsification checks

The two-unit separation in `(12)` is only a normalization. Translating/rescaling the bump locations produces any prescribed positive gap, and the bounds `(5)`--`(6)` scale by that physical separation.

The flat bump is chosen to eliminate boundary-regularity distractions. Both curvature components are `C^\infty`, all derivatives vanish at their endpoints, and `(15)` is stronger than the AF-394 local differential requirement. The failure is therefore not a finite-order boundary singularity of the kind excluded in AF-389.

The counterexample uses a genuine zero interval between curvature components. It does not claim that every disconnected-curvature profile has the same quantitative locality threshold, especially when components meet at an isolated infinitely flat zero rather than a positive-length gap.

The theorem concerns bounded **index radius**, not bounded determinant order alone. Arbitrary prime-ratio `3\times3` minors remain target-complete for the order-three layer by AF-381; the obstruction appears only after imposing local placement compression.

The lower bound `(5)` is one-sided. It says a negative witness must have large index reach, not that every sufficiently large-span stencil is negative.

Equation `(9)` uses the Baker--Harman--Pintz upper bound on prime gaps and is not claimed sharp. Better gap bounds would strengthen the forced index-reach rate without changing the qualitative theorem.

Finally, this is a source-class obstruction on positive smooth translation profiles. An arithmetic source theorem may legitimately exclude the constructed profile by proving connected curvature, analyticity/quasianalytic rigidity across the zero gap, or another global relation. Such a theorem would be exactly the extra fidelity resource the finding says is required.

## Consequence for the line

AF-394 identified connected positive-curvature support as the exact global datum left after the local smooth `PF_3` inequalities are known. AF-395 now shows how that datum behaves under arithmetic-looking local sampling: **it is not recoverable from any bounded successor neighborhood, even as prime-log resolution tends to infinity**.

This closes the most direct order-three extrapolation of AF-382. At order two, nearest-neighbor prime rectangles generate the target. At order three, the unrestricted smooth class requires a qualitatively different resource: either nonlocal placement reach that grows down the prime tail, or source information that forces the missing component topology before the determinant compression is applied.