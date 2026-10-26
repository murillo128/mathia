# AF-591 — Matched prime endpoints admit arbitrarily many crossover minima

## Status and claim

EXACT-DERIVED · NEGATIVE/OBSTRUCTION · GENERALIZED-PRIME-MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

The endpoint constants and positive-source structure retained in
[[research/arithmetic_fidelity/findings/AF-589-prime-window-crossover-is-set-by-the-exact-source-coordinate|AF-589]]
do not bound the number of interior crossover minima. This remains false
after retaining any prescribed finite prime prefix, the exact constant term
at the logarithmic singularity, and both endpoint derivative signs.

Write
\[
 P(s)=\sum_{p\ {\rm prime}}p^{-s},\quad c=e^{B_1},\quad
 a_P(z)=E_1^{-1}(P(1+z)),\quad
 F_P(\tau)=\frac{c\,a_P(2\tau)}{2\tau},
 \qquad z,\tau>0.
 \tag{1}
\]
Here `B_1` is the reciprocal-prime Meissel--Mertens constant and
`E_1(a)=integral_a^infinity exp(-t)dt/t`. The inverse is the positive real
decreasing inverse.

**Theorem.** Given an integer `N>=1`, a prefix cutoff `Y>=2`, a coordinate
cutoff `tau_*>0`, and `0<eta<3/4`, there is a simple unit-weight generalized
prime source
\[
 \mathcal Q=(\mathbb P\setminus S)\cup G,\qquad
 Q(s)=\sum_{q\in\mathcal Q}q^{-s},
 \tag{2}
\]
where `S` is a finite set of rational primes above `Y` and `G` is a finite
set of distinct nonintegral positive rational numbers above `Y`, such that:

1. The removed and added reciprocal masses agree exactly:
   `sum_(p in S) 1/p = sum_(g in G) 1/g`.
2. `Q` has the same convergence boundary `s=1`, the same singular constant
   `Q(1+z)=-log z+B_1-gamma+O(z)`, and the same leading generator `2` with
   coefficient one as `P`.
3. For `a_Q(z)=E_1^(-1)(Q(1+z))` and `F_Q(tau)=c a_Q(2tau)/(2tau)`,
   \[
   F_Q(0+)=1,\qquad F_Q(\infty)=c\log2.
   \tag{3}
   \]
   Nevertheless, `F_Q` has at least `N` distinct strict local minima in
   `(0,tau_*)`, each of value less than `eta`, separated by values greater
   than `3/4`.
4. `F_Q'` is negative sufficiently near zero and positive for
   `tau >= (1+2e)/(2 log 2)`. Each fixed constructed source has only finitely
   many stationary points; the number is unbounded over this matched class.

All coefficients of the actual Dirichlet series in (2) are one. No signed
source, repeated generator, or variable coefficient is used. Generalized
generators need not be ordinary primes or have ordinary unique factorization;
their formal products are counted with their generator provenance, as usual.

This is a counterexample to deducing a single turning point from the listed
retained properties. It does **not** disprove uniqueness for `F_P`, and the
several local minima are not asserted to have equal depth or to be global.

## A finite reciprocal-mass relocation

Fix a positive integer `K` and take a sufficiently large real `r`.
Euler's divergence of the reciprocal-prime sum supplies a finite set `S_r`
of primes with
\[
 \log p\ge r^2\quad(p\in S_r),\qquad
 K\le A_r:=\sum_{p\in S_r}p^{-1}<K+1.
 \tag{4}
\]
For example, start beyond `exp(r^2)` and stop when the partial sum first
reaches `K`. The final summand is less than one. One may also start beyond
any previously selected finite set.

Choose an even integer `m` strictly between `2 A_r e^r` and `3 A_r e^r`;
this is possible for large `r`. There are distinct positive rational numbers
`u_1,...,u_m` with
\[
 \sum_i u_i=A_r,\qquad e^{-r}/4<u_i<e^{-r},
 \qquad g_i:=u_i^{-1}\notin\mathbb Z.
 \tag{5}
\]
Here is an explicit existence argument that does not relax unit weights.
The rational mean `A_r/m` lies strictly between `e^(-r)/3` and `e^(-r)/2`.
Set `u_i=A_r/m+epsilon(i-(m+1)/2)` for a sufficiently small positive
rational `epsilon`. Their sum is unchanged and they are distinct. Because
`m` is even, every perturbation coefficient is nonzero. Only finitely many
choices of `epsilon` make one of the reciprocals an integer in
`(e^r,4e^r)`, so these choices can be avoided. Thus
\[
 e^r<g_i<4e^r<\min S_r
 \tag{6}
\]
for large `r`. All additions and removals may be put above `Y` and above
every earlier block.

The change at `s=1+z` is the entire function
\[
 h_r(z)=\sum_i g_i^{-1}e^{-z\log g_i}
       -\sum_{p\in S_r}p^{-1}e^{-z\log p}.
 \tag{7}
\]
Equal mass and separation of supports give
\[
 h_r(0)=0,\quad h_r(z)>0\ (z>0),\quad
 h_r'(0)=\sum_{p\in S_r}\frac{\log p}{p}
                  -\sum_i\frac{\log g_i}{g_i}>0.
 \tag{8}
\]
The inequalities needed to place one localized depression are
\[
 0<h_r(z)\le(K+1)e^{-rz},\qquad
 h_r(1/r)\ge K\{e^{-1-(\log4)/r}-e^{-r}\}>K/4
 \tag{9}
\]
for sufficiently large `r`. The second lower bound tends to `K/e`, so its
strict comparison with `K/4` does not require a numerical certificate.
Each fixed block also satisfies `h_r(z)->0` as `z->0`. Its value can
therefore be large at an intermediate scale while being arbitrarily small
at any finitely many earlier positive coordinates and at sufficiently small
later coordinates. The source remains positive because the negative terms
remove existing primes exactly once.

## Exact transport through the nonlinear inverse

Let `H` be any finite sum of disjoint relocations (7), and set
`Q(1+z)=P(1+z)+H(z)`. Introduce
\[
 R(a)=\int_0^a\frac{1-e^{-t}}t\,dt,\qquad
 E_1(a)=-\gamma-\log a+R(a).
 \tag{10}
\]
The identity follows either by differentiation and the endpoint limit or
from the classical exponential-integral power series. In particular `R` is
increasing and `0<=R(a)<=a`.

Since `H>=0`, the decreasing inverse gives `a_Q<=a_P`. Subtracting (10)
at these two points, without a linearization, gives
\[
 \log\frac{a_Q(z)}{a_P(z)}
 =-H(z)+R(a_Q(z))-R(a_P(z)).
\]
Consequently, with `z=2tau`,
\[
 \boxed{F_P(\tau)e^{-H(z)-a_P(z)}
            \le F_Q(\tau)\le F_P(\tau)e^{-H(z)}.}
 \tag{11}
\]
The retained reciprocal mass is a constant-term constraint, not a bound on
the intermediate positive perturbation `H`. Equation (11) is the precise
way that this unretained shape passes through the inverse coordinate.

## Separated depressions on an arbitrarily small coordinate interval

Choose an integer `K` with `K/4>log(2/eta)`. By the prime endpoint expansion
in AF-589, choose `0<u_0<2tau_*` such that, for every `0<z<=u_0`,
\[
 7/8<F_P(z/2)<2,\qquad a_P(z)<1/16.
 \tag{12}
\]
Construct finitely many blocks recursively. Before block `j`, assume the
earlier blocks and coordinates have been fixed. Choose `r_j` large enough
that all its generators exceed all previous blocks, `v_j=1/r_j<u_(j-1)`,
and (9) holds. Require also
\[
 (K+1)e^{-r_j u_i}<2^{-j-5}\qquad(0\le i<j).
 \tag{13}
\]
This is a finite list of conditions at positive coordinates. It can always
be met before selecting `S_(r_j)` and `G_(r_j)` by (4)--(6).

Writing `H_j=sum_(k<=j)h_(r_k)`, choose
\[
 0<u_j<v_j,\qquad H_j(u_j)<1/32.
 \tag{14}
\]
Such a choice exists because this is a **finite** sum and `H_j(0)=0`.
No estimate uniform over future blocks is assumed. Instead, (13) controls
those future blocks once they are added.

After `N` steps,
\[
 0<u_N<v_N<u_{N-1}<v_{N-1}<\cdots<u_1<v_1<u_0,
\]
\[
 H_N(u_i)<1/16\quad(0\le i\le N),\qquad
 H_N(v_j)>K/4\quad(1\le j\le N).
 \tag{15}
\]
Indeed, the future contributions at every `u_i` total less than
`sum_(j>=1)2^(-j-5)=1/32`; previous contributions were frozen by (14).
At each `v_j`, all other blocks are nonnegative, so its own lower bound
from (9) survives.

Equations (11)--(15) now imply
\[
 F_Q(u_i/2)>(7/8)e^{-1/8}\ge49/64>3/4,
 \qquad F_Q(v_j/2)<2e^{-K/4}<\eta.
 \tag{16}
\]
On every compact interval `[u_j/2,u_(j-1)/2]`, the minimum is attained in
its interior, below `eta`. The function `Q(1+z)` is real analytic with a
strictly negative derivative; hence `a_Q` and `F_Q` are real analytic for
positive arguments. A nonconstant real analytic function has isolated
interior minimizers, so these include `N` distinct strict local minima.
The intervening high values similarly give at least `N-1` strict local
maxima. No numerical differentiation or sampled-extremum inference enters.

## Endpoint and arithmetic checks

Finite relocation with `H(0)=0` preserves the exact constant term:
\[
 Q(1+z)=-\log z+B_1-\gamma+(C_1+H'(0))z+O(z^2),
 \qquad C_1=\gamma+\sum_p\frac{\log p}{p(p-1)}.
 \tag{17}
\]
The same implicit expansion as AF-589 gives
\[
 F_Q(0+)=1,\qquad F_Q'(0+)=2\{c^{-1}-C_1-H'(0)\}<0.
 \tag{18}
\]
Here `H'(0)>0`, and AF-589 proves `C_1>1>c^(-1)` independently of decimal
evaluation. Higher regular coefficients are **not** being matched.
Beyond the largest changed generator the difference of reciprocal partial
sums is exactly zero, so even the reciprocal-prime Mertens constant agrees
as a partial-sum limit, not just as an Abelian constant.

Every added generator exceeds `2`, and only finitely many are added. Thus
`Q(1+z)~2^(-1-z)` as `z->infinity`. The classical `E_1(a)~e^(-a)/a`
gives `a_Q(z)/z->log2`, proving the other endpoint in (3).

For completeness, put `M_1^Q(z)=sum_(q in Q) (log q)q^(-1-z)` and
`b=z log2`. Differentiation gives
\[
 \operatorname{sgn}F_Q'(z/2)
   =\operatorname{sgn}\{ze^{a_Q}M_1^Q(z)-1\}.
 \tag{19}
\]
When `b>=1+2e`,
`E_1(b-1)<e e^(-b)/(b-1)<=e^(-b)/2<Q(1+z)` implies `a_Q<b-1`.
Also `M_1^Q>=log2 Q` and
`e^a E_1(a)>1/(a+1)`; the latter follows by strict Jensen applied to
`integral_0^infinity e^(-v)/(a+v)dv`. Therefore
\[
 ze^{a_Q}M_1^Q>b/(a_Q+1)>1.
 \tag{20}
\]
This is the same explicit tail sign cutoff as AF-589. Together with (18)
and analyticity it confines each source's stationary points to a compact
subinterval and makes their number finite. The initial sign interval can
shrink as the constructed source changes; no uniform interval is asserted.

There is also a decisive RH control. In the half-plane `Re s>1`, the formal
Euler product of this generalized-prime system equals
\[
 Z_{\mathcal Q}(s)=\zeta(s)
       \frac{\prod_{p\in S}(1-p^{-s})}
            {\prod_{g\in G}(1-g^{-s})}.
 \tag{21}
\]
The finite factor is analytic and nowhere zero on `Re s>0`, since each
generator is greater than one. Equation (21) continues `Z_Q` there and
preserves every zero in `0<Re s<1`, with multiplicity. Thus the crossover
turning geometry can change drastically **while the nontrivial zero set
stays unchanged**. These controls cannot support a claim of RH-relevant
information loss. The discriminator obstructed here is crossover shape.

## Prior art, significance and limits

Euler's reciprocal-prime divergence and the Mertens constant are classical;
see Pollack, [*Euler and the partial sums of the prime harmonic series*](https://ems.press/content/serial-article-files/45523),
*Elemente der Mathematik* 70 (2015), 13--20, especially §2 and the discussion
preceding Theorem 1. Only divergence is needed to select each finite block.
The `E_1` identities and endpoint expansions are classical
[DLMF (6.6.2)](https://dlmf.nist.gov/6.6.E2) and
[(6.12.1)](https://dlmf.nist.gov/6.12.E1).

Yang--Tian, [*Monotonicity rules for the ratio of two Laplace transforms with applications*](https://arxiv.org/abs/1803.02513),
*Journal of Mathematical Analysis and Applications* 470 (2019), 821--845,
study transform-ratio monotonicity with additional order or turning
hypotheses on the underlying densities. Those hypotheses are substantive;
positivity alone is not their conclusion's input, and the nonlinear inverse
ratio in (1) is a different object. No general counterexample priority is
claimed here. The finite relocation, mass balancing, scale separation and
analytic extremum argument are classical methods.

AF-511/512 already use remote finite edits to separate exact provenance from
curvature stability. The distinct result here is an unbounded number of
strict minima for the exact inverse-coordinate crossover, with **exactly
matched** singular constant and smallest-generator data, simple unit weights,
and preserved endpoint derivative signs. Unlike a small relative-curvature
perturbation, the retained crossover changes by a fixed amount at its chosen
intermediate scales. Equation (21) explicitly limits the arithmetic meaning
of that difference.

The actual rational-prime uniqueness question of AF-589 remains open. Its
resolution must use additional source-specific information beyond the matched
properties above. This finding makes no claim about integer-only replacement
generators, a fixed edit budget, prescribed locations of all extrema, equal
global minima, preservation of the full analytic regular germ, or a uniform
initial derivative neighborhood. The finite blocks and their separations can
be enormous. It also does not transfer AF-589's complete polynomial-recovery
theorem to every modified source: the proved target is the exact source
coordinate itself. No formal proof assistant or numerical root certificate
was used; (4)--(21) give the analytic construction and its audits.
