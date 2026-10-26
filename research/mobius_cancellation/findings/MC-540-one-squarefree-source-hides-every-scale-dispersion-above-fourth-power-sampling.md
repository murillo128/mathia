# MC-540 — One square-free source hides every-scale dispersion above fourth-power sampling

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`,
`MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`.

## Claim and retained hypotheses

Fix \(a>4\) and choose
\[
                  \frac34<\kappa<1-\frac1a,\qquad
                  \beta=2\kappa-1>\frac12.
\tag{1}
\]
There is **one deterministic coefficient sequence**
\(f:\mathbb N\to\{-1,0,1\}\), fixed before any observations, with
\[
                         |f(n)|=\mu(n)^2,
\tag{2}
\]
having the following properties. Define
\[
 F(t)=\sum_{n\le t}f(n),\quad S_L(j)=F(j+L)-F(j),\quad
 I_X=\{X,\ldots,2X-1\},
\]
\[
 L_1(X)=\lfloor X/20\rfloor,\qquad
 L_2(X)=\lfloor\sqrt2 L_1(X)\rfloor.
\tag{3}
\]
For **every sufficiently large integer \(X\)**, both channels satisfy
\[
 D_i(X):=X^{-2}\sum_{j,r\in I_X}
       |S_{L_i}(j)-S_{L_i}(r)|\asymp_\kappa X^\beta,
                       \qquad i=1,2.
\tag{4}
\]
All these populations arise from the same prefix \(F\); in particular
their compatibility holds across overlapping scales and lengths.
Their consecutive jumps are at most two.

At each prescribed \(X_k=\lceil k^a\rceil\), draw two uniform
starts in each channel and let
\[
 V_i(k)=\frac14
   |S_{L_i}(R_{i,k,1})-S_{L_i}(R_{i,k,2})|^2.
\tag{5}
\]
With probability one, along the **whole** prescribed sequence,
\[
                         V_1(k),V_2(k)\le1
                         \quad\text{eventually}.
\tag{6}
\]
In fact all four observed window values eventually belong to
\(\{-1,0,1\}\). Independent draws with replacement are allowed,
but (6) needs only uniform marginal laws, even with dependence across
channels and scales. The source never depends on the draws.

[MC-539](MC-539-two-random-starts-detect-mobius-poles-on-fourth-power-scales.md)
proved the fourth-power detection threshold from bounded jumps and
an every-block dispersion floor; its faster-scale control assigned
separate populations at each scale. Here that obstruction persists
after imposing one common coefficient source and exact square-free
magnitudes. The construction is **not multiplicative**, and no
reciprocal-zeta identity or pole-isolating smooth asymptotic is
asserted. Thus (6) is not a counterexample to a Möbius criterion.

## 1. A single infinite family of balanced square-free bridges

Let
\[
 Q(n)=\sum_{r\le n}\mu(r)^2,\qquad B(n)=Q(n)\bmod2\in\{0,1\},
 \qquad b(n)=B(n)-B(n-1).
\tag{7}
\]
The baseline \(b\) alternates signs on the square-free integers and
vanishes elsewhere. Every interval sum is at most one in absolute value.

For all integers \(m\ge m_0\), put
\[
 c_m=\lfloor(3/2)^m\rfloor,\qquad
 w_m=\lfloor c_m^\kappa/100\rfloor,\qquad
 J_m=\{c_m,\ldots,c_m+w_m\}.
\tag{8}
\]
Choose a fixed sufficiently large \(m_0\) so the blocks are disjoint.
Their widths are \(o(c_m)\), while adjacent centers are separated by
\(\asymp c_m\). No choice depends on a sample or a scale cutoff.

In \(J_m\), list the square-free positions
\(t_1<\cdots<t_{N_m}\), and put \(r_m=\lfloor N_m/2\rfloor\).
Replace the baseline signs on the first \(2r_m\) positions by
\[
 f(t_j)=
 \begin{cases}
  +1,&1\le j\le r_m,\\
  -1,&r_m<j\le2r_m.
 \end{cases}
\tag{9}
\]
Leave an optional last square-free position at its baseline sign;
leave all other coefficients equal to \(b\). This defines one
infinite sequence, because the blocks are disjoint.

The overwritten even string and the original alternating string both
have total zero. Therefore
\[
                         F(n)=B(n)\quad(n\notin\cup_m J_m),
\tag{10}
\]
and (2) holds identically. Set \(e_m=B(c_m-1)\). Before the final
even active position, \(F-e_m\) is the nonnegative bridge whose
values at the active positions are
\[
                        \min(j,2r_m-j).
\]
Define \(H_m(n)=F(n)-e_m\) for
\(c_m\le n<t_{2r_m}\), and zero otherwise; omit the bridge if
\(r_m=0\). Then \(F(n)\ge H_m(n)\) on \(J_m\), and
\[
       \sum_{n\in J_m}H_m(n)\ge
       \sum_{j=1}^{2r_m-1}\min(j,2r_m-j)=r_m^2,
       \qquad 0\le F(n)\le r_m+1\quad(n\in J_m).
\tag{11}
\]
The inequality uses only that consecutive active positions are at
least one integer apart. An odd final position merely restores the
appropriate baseline parity and cannot remove this area.

For completeness, the elementary square-free estimate is
\[
 Q(y)=\sum_{d\le\sqrt y}\mu(d)\lfloor y/d^2\rfloor
     =\frac{y}{\zeta(2)}+O(\sqrt y).
\tag{12}
\]
The floor errors total \(O(\sqrt y)\), and the absolutely convergent
tail of \(\sum_d\mu(d)/d^2\) costs the same after multiplication
by \(y\). Thus, since \(\kappa>1/2\),
\[
 N_m=\frac{w_m+1}{\zeta(2)}+O(\sqrt{c_m}),\qquad
                    r_m\asymp w_m\asymp c_m^\kappa.
\tag{13}
\]
This uses no delicate short-interval square-free theorem. The prefix
also attains size \(\gg c_m^\kappa\) near each bridge's middle.

## 2. Both actual window channels have dispersion on every block

For each large integer \(X\), choose the least \(m\) with
\(c_m\ge5X/4\). Rounding in (8) gives
\[
                    5X/4\le c_m<15X/8+2.
\tag{14}
\]
Hence \(J_m\subset I_X\) for all sufficiently large \(X\).
For either length in (3), \(w_m<L_i\) and
\[
                (J_m+L_i)\cap\bigcup_\ell J_\ell=\varnothing.
\tag{15}
\]
Indeed, the translation clears \(J_m\) because \(w_m=o(X)\),
and the next center is at distance \(c_m/2+O(1)\), much greater
than \(L_i+w_m\le(\sqrt2/20+o(1))X\). Previous blocks lie
to its left. Therefore, for \(j\in J_m\),
\[
                     S_{L_i}(j)\le1-H_m(j).
\tag{16}
\]

Let \(G_i(X)\) be the starts in \(I_X\) for which neither
\(j\) nor \(j+L_i\) belongs to any \(J_\ell\). Only
\(O(1)\) geometric blocks meet the endpoint range
\([X,2X+L_i]\); their centers are \(\asymp X\) and their
total width is \(O_\kappa(X^\kappa)\). Consequently
\[
 |I_X\setminus G_i(X)|=O_\kappa(X^\kappa),\qquad
 |S_{L_i}(r)|\le1\quad(r\in G_i(X)).
\tag{17}
\]
The sets \(J_m\) and \(G_i(X)\) are disjoint. Counting both
orientations of their pairs, (11) and (16) imply
\[
 \begin{split}
 D_i(X)&\ge\frac{2|G_i(X)|}{X^2}
              \sum_{j\in J_m}(H_m(j)-2)\\
       &\ge\frac{2|G_i(X)|}{X^2}
                  \bigl(r_m^2-2(w_m+1)\bigr)
        \gg_\kappa X^{2\kappa-1}.
 \end{split}
\tag{18}
\]
Negative terms in this finite lower bound cause no issue; its final
bracket is positive at sufficiently large scales by (13).

For the matching upper bound, (10)–(13) show that
\(F(n)\le1+O_\kappa(X^\kappa)\) throughout the relevant endpoint
range, and \(F(n)\in\{0,1\}\) outside its
\(O_\kappa(X^\kappa)\) exceptional positions. Thus
\[
 X^{-1}\sum_{j\in I_X}|S_{L_i}(j)|
       \ll_\kappa 1+X^{2\kappa-1}.
\]
The triangle inequality gives the upper half of (4). Finally,
\(S_L(j+1)-S_L(j)=f(j+L+1)-f(j+1)\), proving the jump bound.
No independent specification of a population has entered this argument.

## 3. Summable endpoint hits leave all observed windows small

Let \(E_k\) be the event that at least one of the four observed
starts lies outside its corresponding \(G_i(X_k)\). Uniform
marginals and (17), with a union bound, give
\[
                  \Pr(E_k)\ll_\kappa X_k^{\kappa-1}.
\tag{19}
\]
The exponent choice (1) ensures
\[
                     \sum_k\Pr(E_k)
                      \ll\sum_k k^{-a(1-\kappa)}<\infty.
\tag{20}
\]
The first Borel–Cantelli lemma implies that only finitely many
\(E_k\) occur, without independence assumptions. On \(E_k^c\),
every queried value lies in \(\{-1,0,1\}\); (6) follows.
More generally, the same fixed source works on any deterministic
scale sequence satisfying \(\sum_k X_k^{\kappa-1}<\infty\).
No post-selection of favorable scales is used.

## Prior art, validation, and consequence

The hidden-area mechanism is classical Lipschitz sampling geometry:
[Baran–Demaine–Katz, Section 2](https://erikdemaine.org/papers/Integration_Algorithmica/paper.pdf)
(MC-S85). Disjoint bumps are also standard in randomized integration
lower bounds; compare
[Kunsch–Rudolf, Section 2.1, Lemmas 2.1–2.2](https://arxiv.org/html/1809.09890v1)
(MC-S93). Those results provide methodological prior art, not the
arithmetic or infinite-scale assertion here. The elementary counting
input (12) is classical (MC-S12), and the probability step is precisely
[Durrett, Theorem 2.3.1](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf)
(MC-S92). No new counting, integration, probability principle, or
external novelty is claimed.

Internally, [MC-534](MC-534-common-squarefree-coefficients-retain-signed-sampling-ambiguity.md)
already realizes square-free bridges with prescribed interval-endpoint
matching, including separated-scale controls. Its signs may depend
on those prescribed queries. [MC-538](MC-538-one-fixed-multiplicative-source-defeats-subquarter-random-observations.md)
retains multiplicativity for one source on lacunary scales. Neither
supplies the simultaneous all-integer-scale dispersion and
sample-independent polynomial-scale invisibility proved here.

Exact finite checks covered all 16,380 support/parity configurations
in blocks of lengths one through twelve, verifying endpoint matching
and (11). A square-free sieve and exact integer prefix construction
through 1,100,000, using 19 geometric bridges at \(\kappa=4/5\),
verified coefficient magnitudes and baseline recovery everywhere.
Twenty channel/block checks verified (15), (17), the jump bound and
the finite inequality in (18), computing pair dispersion by the
sorted-value identity
\(\sum_{j,r}|u_j-u_r|=2\sum_{j=0}^{X-1}(2j-X+1)u_{(j)}\).
Five rational choices of \(a>4\) checked the strict exponent interval.
These checks audit finite bookkeeping, not the infinite-scale
asymptotic or a Möbius assertion; those rest on the displayed proof.
No formal verification or independent adversarial approval is claimed.

The mathematical delta is the removal of the **separate-populations
loophole** in MC-539's generic obstruction. Common coefficients,
exact square-free support, overlapping-scale consistency and
an every-scale dispersion floor still cannot extend that generic
two-start detector beyond fourth-power scale spacing. At \(a=4\)
the interval (1) is empty, in agreement with MC-539.

The remaining distinction is arithmetic: this source does not obey
multiplicativity, Möbius prime signs, or the exact reciprocal-zeta
pole-test relation. In particular, a dispersion floor is only a
consequence of that relation, not an equivalent replacement for it.
The result does not show optimal sampling for actual Möbius, does
not bound its observed energies, and does not control a fixed signed
smooth test on every scale. A multiplicative control with this dense
scale coverage, or a positive theorem using additional arithmetic
structure, remains outside the claim. The classical finite bridge
lemma alone supplies no separate high-value formalization target.
