# FD-053 — growing primorial Jordan rays preserve squarefree self-cancellation to the square-root boundary

**Status:** `EXACT-DERIVED + MOVING-DILATION + UNIFORM-WIENER-DIRICHLET-BOUND + SQUAREFREE-PRESERVING-RAY + PRIMORIAL-ROUGH-CASCADE + SQUARE-ROOT-ROW-BOUNDARY + FALSE-RH-SELF-CANCELLATION + NEGATIVE/ROUTE-RESTRICTION`.

`FD-052` shows that for every **fixed** squarefree host row `q`, the Jordan-weighted first-moment ray through the physical shell source cancels the source factor `1/zeta(s)`. Under false RH, a `Theta`-scale spike on that row is therefore balanced to leading order by other squarefree rows rather than by the nonsquarefree branch. The remaining occupation frontier, however, is no longer confined to fixed rows: `FD-051` pushes the universal terminal occupation barrier down to the square-root row scale, while the unresolved escape lives on the growing low-row side of that boundary.

The fixed-`q` restriction in `FD-052` is not a genuine protection. The same Euler product admits a uniform Wiener--Dirichlet estimate whose only nontrivial host cost is

\[
P_\sigma(q):=\sum_{p\mid q}p^{-\sigma},
\qquad \sigma>\frac12.
\]

For every squarefree `q`, if

\[
\mathscr R_q^{\rm sf}(X)
:=
\sum_{\substack{m\le X\\\mu(qm)\ne0}}
 w(qm)\,
 \mathcal H\!\left(\left\lfloor\frac Xm\right\rfloor\right),
\qquad
w(n):=\frac{J_2(n)}{n^2},
\]

then

\[
\boxed{
|\mathscr R_q^{\rm sf}(X)|
\ll_\sigma
X^\sigma(1+\log X)
\exp\!\bigl(C_\sigma P_\sigma(q)\bigr).
}
\tag{1}
\]

The corresponding **complete** ray satisfies the stronger host-uniform estimate

\[
\boxed{
|\mathscr R_q(X)|
\ll_\sigma X^\sigma(1+\log X)
}
\tag{2}
\]

for every integer `q>=1`, with an implied constant independent of `q`. Consequently the nonsquarefree-output ray

\[
\mathscr R_q^{\rm ns}(X)
:=\mathscr R_q(X)-\mathscr R_q^{\rm sf}(X)
\]

obeys the same bound as (1).

This makes the false-RH self-cancellation of `FD-052` stable under a large class of **moving** host rows. If `Theta>1/2`, choose

\[
\frac12<\sigma<\Theta-\delta
\]

and let `X_j` be any zero-frontier spike sequence with

\[
|\mathcal H(X_j)|\ge X_j^{\Theta-\delta}.
\]

For arbitrary squarefree hosts `q_j` satisfying

\[
\boxed{P_\sigma(q_j)=o(\log X_j),}
\tag{3}
\]

one has

\[
\boxed{
\mathscr R_{q_j}^{\rm sf}(X_j)
=o(|\mathcal H(X_j)|),
\qquad
\mathscr R_{q_j}^{\rm ns}(X_j)
=o(|\mathcal H(X_j)|),
}
\tag{4}
\]

and therefore, after removing the `m=1` term,

\[
\boxed{
\sum_{\substack{2\le m\le X_j\\\mu(q_jm)\ne0}}
 w(q_jm)
 \mathcal H\!\left(\left\lfloor\frac{X_j}{m}\right\rfloor\right)
=
-w(q_j)\mathcal H(X_j)
+o(|\mathcal H(X_j)|).
}
\tag{5}
\]

The condition (3) allows hosts all the way to the geometric boundary isolated by `FD-051`. Fix `0<c<=1` and take the primorial host

\[
q_X:=\prod_{p\le c\log X}p.
\tag{6}
\]

Then for every fixed `sigma>1/2`,

\[
P_\sigma(q_X)
\le
\sum_{n\le c\log X}n^{-\sigma}
\ll_\sigma
(\log X)^{1-\sigma}
=o(\log X),
\tag{7}
\]

so (4)--(5) apply. By the prime number theorem,

\[
q_X=X^{c+o(1)}.
\tag{8}
\]

At the physical horizon

\[
H_X:=q_XX,
\]

the host row therefore lies at

\[
\boxed{
q_X=H_X^{\,c/(1+c)+o(1)}.
}
\tag{9}
\]

As `c` ranges over `(0,1]`, the exponent `c/(1+c)` fills `(0,1/2]`. In particular `c=1` places the host at

\[
\boxed{q_X=H_X^{1/2+o(1)},}
\tag{10}
\]

exactly the square-root row boundary where source-independent terminal occupation ceases to be uniform.

There is also a scale-separation feature absent from the fixed-host statement. Because every prime `p<=c log X` divides `q_X`, the squarefree-preserving descendants in (5) have

\[
(m,q_X)=1,
\qquad \mu(m)^2=1.
\]

Thus every `m>1` occurring in the cancellation has least prime factor exceeding `c log X`, hence

\[
\boxed{
m>c\log X,
\qquad
\left\lfloor\frac Xm\right\rfloor
\le \frac{X}{c\log X}.}
\tag{11}
\]

So an off-critical spike on a growing low row can, at signed first-moment level, be cancelled entirely by **squarefree descendants whose shell arguments already lie a logarithmic factor below the spike scale**. No small-prime square divisor is needed to transport the leading response.

This remains a negative/route-restriction result, not a construction of `U_(H,D)/E_(H,D)->0`. Equations (4)--(5) are signed identities; the terminal rows participating in the squarefree cancellation may simultaneously coexist with the positive nonsquarefree quadratic mass forced by `FD-051`. What the result removes is a plausible loophole in `FD-052`: letting the host row grow, even up to `H^(1/2+o(1))`, does not by itself make the exact Jordan/divisibility **linear** carrier sensitive to the zeta-zero pole. The remaining occupation theorem must use positivity/quadratic information, a bilinear coupling between rays, or a constraint stronger than any first moment controlled by the same zeta-factor Wiener algebra.

## 1. Uniformizing the squarefree-preserving Euler factor

Retain the physical coefficient sequence

\[
\sum_{n\ge1}\frac{c(n)}{n^s}
=
\frac{\zeta(s+1)}{\zeta(s)},
\qquad
\mathcal H(X)=\sum_{n\le X}c(n).
\tag{12}
\]

For squarefree `q`, `FD-052` gives

\[
A_q^{\rm sf}(s)
:=
\sum_{\substack{m\ge1\\\mu(qm)\ne0}}
\frac{w(qm)}{m^s}
=
\zeta(s)B_q(s),
\tag{13}
\]

where

\[
B_q(s)
=
w(q)A(s)
\prod_{p\mid q}
\left(1+(1-p^{-2})p^{-s}\right)^{-1},
\tag{14}
\]

and `A(s)` has an absolutely convergent Dirichlet series throughout every half-plane `Re(s)>1/2`.

For a Dirichlet series

\[
B(s)=\sum_{d\ge1}\frac{b(d)}{d^s},
\]

write its Wiener norm on the line `Re(s)=sigma` as

\[
\|B\|_\sigma
:=
\sum_{d\ge1}\frac{|b(d)|}{d^\sigma}.
\tag{15}
\]

Absolute Dirichlet series form a Banach algebra under multiplication. The local inverse in (14) has norm

\[
\left\|
\left(1+(1-p^{-2})p^{-s}\right)^{-1}
\right\|_\sigma
=
\frac1{1-(1-p^{-2})p^{-\sigma}}.
\tag{16}
\]

Since `sigma>1/2`, and `p^(-sigma)<=2^(-sigma)<1`,

\[
-\log\!\left(1-(1-p^{-2})p^{-\sigma}\right)
\le C_\sigma p^{-\sigma}.
\tag{17}
\]

Using `w(q)<=1`, equations (14)--(17) give the uniform host-complexity estimate

\[
\boxed{
\|B_q\|_\sigma
\le
\|A\|_\sigma
\exp\!\bigl(C_\sigma P_\sigma(q)\bigr).
}
\tag{18}
\]

The fixed-`q` constant in `FD-052` is therefore completely explicit in the only direction that can grow dangerously.

## 2. Floor convolution turns the Wiener norm into a uniform ray bound

Multiplying (13) by the physical source series (12) cancels `zeta(s)` exactly:

\[
A_q^{\rm sf}(s)
\frac{\zeta(s+1)}{\zeta(s)}
=
\zeta(s+1)B_q(s).
\tag{19}
\]

If

\[
B_q(s)=\sum_{d\ge1}\frac{b_q(d)}{d^s},
\]

then the same floor-convolution identity as in `FD-052` gives

\[
\boxed{
\mathscr R_q^{\rm sf}(X)
=
\sum_{d\le X}
 b_q(d)
 \mathbf H_{\lfloor X/d\rfloor},
}
\tag{20}
\]

where `mathbf H_n=sum_(k<=n)1/k` is the ordinary harmonic number. Hence

\[
\begin{aligned}
|\mathscr R_q^{\rm sf}(X)|
&\le
(1+\log X)
\sum_{d\le X}|b_q(d)|\\
&\le
X^\sigma(1+\log X)\|B_q\|_\sigma.
\end{aligned}
\tag{21}
\]

Equation (1) follows from (18).

For the complete ray, `FD-052` gives

\[
A_q(s)\frac{\zeta(s+1)}{\zeta(s)}
=
\zeta(s+1)D_q(s),
\tag{22}
\]

with

\[
D_q(s)
=
\frac{w(q)}{\zeta(s+2)}
\prod_{p\mid q}(1-p^{-(s+2)})^{-1}.
\tag{23}
\]

The first factor has finite Wiener norm already for `sigma>-1`, while

\[
\prod_{p\mid q}(1-p^{-(\sigma+2)})^{-1}
\le \zeta(\sigma+2).
\tag{24}
\]

Thus

\[
\boxed{
\sup_{q\ge1}\|D_q\|_\sigma<\infty
}
\tag{25}
\]

for every fixed `sigma>1/2`. Repeating (20)--(21) proves (2), and subtraction proves the asserted nonsquarefree-ray bound.

## 3. False RH still self-cancels for moving hosts

Let

\[
\Theta
:=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

Assume `Theta>1/2`. Fix `delta>0` small enough that `Theta-delta>1/2`, then choose

\[
\frac12<\sigma<\Theta-\delta.
\tag{26}
\]

`FD-046` gives arbitrarily large `X_j` satisfying

\[
|\mathcal H(X_j)|\ge X_j^{\Theta-\delta}.
\tag{27}
\]

Let `q_j` be squarefree and satisfy (3). Equations (1)--(3) imply

\[
|\mathscr R_{q_j}^{\rm sf}(X_j)|
\le X_j^{\sigma+o(1)}
=o(X_j^{\Theta-\delta}),
\tag{28}
\]

while (2) gives the same estimate for the complete ray. This proves (4). Since

\[
w(q_j)
=\prod_{p\mid q_j}(1-p^{-2})
\ge\prod_p(1-p^{-2})
=\frac1{\zeta(2)},
\tag{29}
\]

the `m=1` term is uniformly comparable to the spike itself. Removing it from the first relation in (4) proves (5).

The lower bound (29) is important when the host moves: no amplitude is lost by accumulating more prime factors in `q_j`.

## 4. Primorial hosts reach every polynomial low-row depth through the square-root endpoint

Take (6). The complexity condition is elementary: for every `sigma in (1/2,1)`,

\[
P_\sigma(q_X)
\le1+\int_1^{c\log X}t^{-\sigma}\,dt
=O_\sigma((\log X)^{1-\sigma}),
\tag{30}
\]

which is `o(log X)`. Thus the moving-host cancellation theorem applies without any distribution theorem for primes.

To locate the host row relative to the physical horizon, use only the prime number theorem already anchored in `SOURCES.md`:

\[
\log q_X
=\vartheta(c\log X)
=c\log X+o(\log X).
\tag{31}
\]

Equations (8)--(10) follow. More explicitly, for every desired row exponent

\[
0<\alpha\le\frac12,
\]

choose

\[
c=\frac{\alpha}{1-\alpha}\in(0,1].
\tag{32}
\]

Then

\[
q_X=H_X^{\alpha+o(1)}.
\tag{33}
\]

So the linear squarefree escape in `FD-052` is not a fixed-low-row artifact. It survives at every polynomial host depth on the unresolved side of the terminal theorem and reaches the `H^(1/2+o(1))` boundary itself.

## 5. Rough descendants create a logarithmically separated cancellation cascade

For the primorial host, `mu(q_Xm)!=0` means both that `m` is squarefree and that no prime dividing `q_X` divides `m`. Therefore every nontrivial descendant has least prime factor greater than `c log X`, which proves (11).

At horizon `H_X=q_XX`, the host row `q_X` samples exactly `mathcal H(X)`. Equation (5) says that its leading off-critical value is balanced by squarefree rows `q_Xm`, yet every one of those rows samples a shell argument at most `X/(c log X)`. Thus the cancellation can jump directly across a logarithmic gap in shell scale while avoiding every prime-square output row.

This observation should not be iterated as though (5) supplied a pointwise recursion for each descendant: it is one signed aggregate identity, and the individual lower-scale terms can themselves have complicated cancellation. The durable conclusion is only that neither a growing host nor exclusion of all small-prime descendants turns this first moment into a nonsquarefree coercive statistic.

## 6. Prior-art boundary and falsification checks

The proof uses only standard absolute-convergence algebra for Dirichlet series plus the Euler products already derived in `FD-044` and `FD-052`. A targeted search for Jordan-totient/squarefree Dirichlet products, Wiener--Dirichlet algebras, and Farey--Mertens dilation identities located the expected general theory of absolutely convergent Dirichlet-series algebras and standard convolution identities, but no result matching the present moving-host physical ray or the primorial placement at the square-root Farey/Jordan boundary. No new external theorem is load-bearing; the only asymptotic used to translate a primorial into a row exponent is the prime number theorem already anchored in `SOURCES.md`. Therefore `SOURCES.md` requires no addition.

The main falsification checks concern uniformity. Equation (18) is valid only for `sigma>1/2`, because the squarefree factor `A(s)` is known in the required absolute Wiener class only there. The moving-host condition is not `q=X^{o(1)}`; the correct complexity is the softer prime-support quantity `P_sigma(q)=o(log X)`, so very large squarefree hosts with sparse prime support are also allowed. Conversely, a host whose small-prime support makes `P_sigma(q)` comparable to `log X` is outside the negligible-response conclusion unless the constants are tracked more sharply.

Finally, (5) is a signed first-moment statement. It neither lowers the positive nonsquarefree energy nor conflicts with `FD-051`. The square-root coincidence identifies a sharp **route boundary**: source-independent positivity survives below that scale, while source-specific linear self-cancellation also survives up to it. Any resolution of the accepted occupation clue must separate those two facts using genuinely quadratic or sign-sensitive structure rather than another zeta-factor row sum.