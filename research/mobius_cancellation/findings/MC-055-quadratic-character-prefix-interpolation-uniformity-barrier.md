# MC-055 — Quadratic-character interpolation gives exact-prefix square-root comparators only nonuniformly

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

For every finite observation scale

\[
X\ge 2,
\]

there exists an odd prime modulus `q_X>X` and its primitive quadratic character

\[
\chi_X(n)=\left(\frac{n}{q_X}\right)
\]

such that

\[
\chi_X(p)=-1
\qquad\text{for every prime }p\le X.
\tag{1}
\]

Define the multiplicative square-free-supported comparator

\[
f_X(n)=\mu(n)^2\chi_X(n),
\qquad
S_X(y)=\sum_{n\le y}f_X(n).
\tag{2}
\]

Then the comparator agrees **exactly** with Möbius on the whole observed prefix:

\[
\boxed{f_X(n)=\mu(n)\quad(1\le n\le X),}
\qquad
\boxed{S_X(X)=M(X).}
\tag{3}
\]

Nevertheless every fixed comparator `f_X` has an unconditional square-root **power exponent** for its own partial sums:

\[
\boxed{|S_X(y)|\ll \sqrt{q_X}\log q_X\,\sqrt y
\qquad(y\ge1).}
\tag{4}
\]

The constant in `(4)` depends on the moving conductor `q_X`. That dependence is not cosmetic. If

\[
C_X(\varepsilon)
:=
\sup_{y\ge1}
\frac{|S_X(y)|}{y^{1/2+\varepsilon}},
\tag{5}
\]

then exact prefix agreement gives the unavoidable lower bound

\[
\boxed{
C_X(\varepsilon)
\ge
\frac{|M(X)|}{X^{1/2+\varepsilon}}.
}
\tag{6}
\]

Thus a family-uniform estimate `C_X(epsilon)=O_epsilon(1)`, or even a sufficiently uniform `X^{o(1)}` estimate after the usual epsilon relabeling, would already give RH-scale Mertens cancellation. Merely producing, for every `X`, a scale-dependent multiplicative object that agrees locally with Möbius and has a fixed-function exponent `1/2` is therefore **not** a cheaper transfer mechanism. The missing information has moved into uniform control of the comparator certificate.

The global analytic boundary makes the same point from another direction. For each fixed `X`,

\[
F_X(s):=\sum_{n\ge1}\frac{f_X(n)}{n^s}
=
\frac{L(s,\chi_X)}{L(2s,\chi_X^2)}
\qquad(\operatorname{Re}s>1),
\tag{7}
\]

and, because `chi_X` is nonprincipal,

\[
\boxed{F_X(1)\ne0.}
\tag{8}
\]

So these comparators evade the fixed-comparator obstructions in `MC-050`--`MC-054` precisely by failing their **global** boundary/closeness hypotheses, even though no coefficient or prime-power datum up to scale `X` can distinguish them from Möbius.

This is a matched-control obstruction, not a new estimate for `M(x)` and not a novelty claim for the classical ingredients.

## 1. A quadratic character can be forced to equal `-1` on every prime up to `X`

Let

\[
M_X=8\prod_{3\le p\le X}p,
\]

where the product is over odd primes. For each odd prime `p<=X`, choose one quadratic nonresidue `a_p mod p`. By the Chinese remainder theorem there is a residue class `a mod M_X` satisfying

\[
a\equiv5\pmod 8,
\qquad
a\equiv a_p\pmod p
\quad(3\le p\le X,\ p\text{ prime}).
\tag{9}
\]

Every chosen `a_p` is nonzero modulo `p`, and `a` is odd, hence

\[
(a,M_X)=1.
\]

Dirichlet's theorem on primes in arithmetic progressions therefore supplies infinitely many primes

\[
q\equiv a\pmod{M_X}.
\tag{10}
\]

Choose one and call it `q_X`. Since every prime at most `X` divides `M_X` while `q_X` is coprime to `M_X`, necessarily

\[
q_X>X.
\tag{11}
\]

Equation `(9)` gives `q_X≡5 mod 8`, hence `q_X≡1 mod 4` and the supplementary law gives

\[
\left(\frac{2}{q_X}\right)=-1.
\tag{12}
\]

For every odd prime `p<=X`, quadratic reciprocity has no sign because `q_X≡1 mod4`, so

\[
\left(\frac{p}{q_X}\right)
=
\left(\frac{q_X}{p}\right)
=
\left(\frac{a_p}{p}\right)
=-1.
\tag{13}
\]

This proves `(1)`. The Legendre symbol modulo the prime `q_X` is a nonprincipal primitive Dirichlet character.

Nothing quantitative about the least possible `q_X` is used. That absence of conductor control is intentional: it is exactly where the later uniformity obstruction lives.

## 2. The comparator is indistinguishable from Möbius on the entire finite prefix

Take `n<=X`. Since `q_X>X`, no prime factor of `n` is the conductor prime.

If `n` is not square-free, both sides of

\[
f_X(n)=\mu(n)
\]

are zero. If `n` is square-free, write

\[
n=p_1\cdots p_k.
\]

Complete multiplicativity of the character and `(1)` give

\[
\chi_X(n)
=
\prod_{j=1}^k\chi_X(p_j)
=(-1)^k
=
\mu(n).
\tag{14}
\]

Since `mu(n)^2=1` in this case, `(2)` and `(14)` prove `(3)`.

This is stronger than the one-scale small-distance controls of `MC-045` and `MC-046`. Here every coefficient through the observation scale is exactly the same. In particular, any diagnostic depending only on local Euler data at primes and prime powers `<=X`, any finite-prefix correlation statistic, and any truncated ordinary or strong pretentious carrier built solely from that observed arithmetic data sees **zero discrepancy** between `f_X` and Möbius.

The difference is entirely beyond the current observation boundary.

## 3. Each fixed comparator has square-root partial-sum exponent

Use the classical identity

\[
\mu(n)^2=\sum_{d^2\mid n}\mu(d).
\tag{15}
\]

Then

\[
\begin{aligned}
S_X(y)
&=
\sum_{n\le y}\chi_X(n)
\sum_{d^2\mid n}\mu(d)\\
&=
\sum_{\substack{d\le\sqrt y\\q_X\nmid d}}
\mu(d)
\sum_{m\le y/d^2}\chi_X(m).
\end{aligned}
\tag{16}
\]

When `q_X|d`, the character factor vanishes and those terms disappear. Since `chi_X` is primitive and nonprincipal, the Pólya--Vinogradov inequality gives uniformly in `T`

\[
\left|\sum_{m\le T}\chi_X(m)\right|
\ll
\sqrt{q_X}\log q_X.
\tag{17}
\]

Applying `(17)` termwise in `(16)` yields

\[
|S_X(y)|
\ll
\sqrt{q_X}\log q_X
\sum_{d\le\sqrt y}1
\ll
\sqrt{q_X}\log q_X\,\sqrt y,
\]

which is `(4)`.

Thus every frozen comparator has a theorem at the critical **exponent** without any assumption on zeta zeros. But the theorem is parameterized by a conductor selected to encode the observation prefix. It supplies no scale-uniform critical estimate for the family.

This separates two statements that a comparator argument must not conflate:

- `for each X there exists f_X with a square-root exponent`; and
- `there is a square-root estimate for f_X at scale X with constants controlled uniformly enough to transfer back to M(X)`.

Only the second would carry useful Mertens information.

## 4. Uniform comparator constants already contain the Mertens target

For every `epsilon>0`, the Pólya--Vinogradov estimate makes `C_X(epsilon)` in `(5)` finite. But `(3)` immediately gives

\[
C_X(\varepsilon)
\ge
\frac{|S_X(X)|}{X^{1/2+\varepsilon}}
=
\frac{|M(X)|}{X^{1/2+\varepsilon}},
\]

proving `(6)`.

Consequently, if one could prove from independently weaker arithmetic that

\[
C_X(\varepsilon)\ll_\varepsilon1
\quad\text{uniformly in }X,
\tag{18}
\]

then

\[
M(X)=O_\varepsilon(X^{1/2+\varepsilon}),
\]

which is the standard RH-equivalent Mertens bound.

More generally, a family estimate

\[
C_X(\varepsilon)=X^{o(1)}
\tag{19}
\]

can be absorbed by an arbitrarily small exponent loss and again reaches the RH boundary after relabeling epsilon. So any claimed scale-dependent comparator bootstrap must audit not only the comparator's asymptotic exponent but the dependence of its constants on the scale-dependent object used to manufacture local agreement.

The generic certificate `(4)` gives only

\[
C_X(0)\ll\sqrt{q_X}\log q_X,
\tag{20}
\]

and the construction provides no useful relation between that conductor factor and the observation scale. Equation `(20)` is an upper bound, not a claim that the true constant must have that size. The exact lower bound relevant to transfer is `(6)`.

## 5. Perfect finite-prefix agreement does not force the global boundary zero

For `Re(s)>1`, square-free support and complete multiplicativity of `chi_X` give

\[
F_X(s)
=
\prod_p(1+\chi_X(p)p^{-s}).
\tag{21}
\]

For `p\ne q_X`, one has `chi_X(p)^2=1`, so

\[
1+\chi_X(p)p^{-s}
=
\frac{1-p^{-2s}}{1-\chi_X(p)p^{-s}}.
\]

At `p=q_X` both relevant character Euler factors are `1`. Hence

\[
F_X(s)
=
\frac{L(s,\chi_X)}{L(2s,\chi_X^2)},
\]

which is `(7)`. Here `chi_X^2` is the principal character modulo `q_X`, so

\[
L(2s,\chi_X^2)
=
\zeta(2s)(1-q_X^{-2s}).
\tag{22}
\]

The denominator is finite and nonzero at `s=1`. The classical Dirichlet nonvanishing theorem gives

\[
L(1,\chi_X)\ne0
\]

for every nonprincipal character. Therefore `(8)` follows.

This is the exact global datum that the finite prefix cannot see. `MC-050`--`MC-053` show that, for fixed square-free-supported comparators, a power bound plus the appropriate global Möbius-closeness/boundary-zero condition forces a matching zeta zero-free region. The present family avoids that conclusion not by beating those theorems, but by making the local relation perfect while leaving the global boundary condition false.

Similarly, the global ordinary pretentious distance from Möbius is not finite: for primes with `chi_X(p)=+1`, the local discrepancy from `mu(p)=-1` contributes `2/p`, and the reciprocal-prime mass in those quadratic residue classes diverges. That is consistent with the fixed global-closeness hypotheses in the previous findings being genuinely load-bearing.

## 6. Relation to the current comparator frontier

`MC-045` showed that ordinary one-scale pretentiousness can be asymptotically blind to a coherent terminal-prime perturbation. `MC-047` repaired that particular blindness with the Jung--Lemke Oliver strong power-aware carrier: on the terminal slab its cost matches the endpoint defect at target normalization. The current construction is a different control. Because `f_X` and Möbius have identical local Euler factors at every prime `p<=X`, **every** such truncated power-aware carrier is exactly zero there. No stronger weighting of already-observed primes can recover information that has been moved entirely beyond the cutoff.

`MC-049`--`MC-054` then closed several fixed globally close comparator classes: independently proving a power exponent for a fixed comparator plus enough global proximity/boundary information already forces the matching zeta zero-free half-plane. `MC-054` explicitly left scale-dependent/local relations as a surviving category. The present finding narrows that category: local identity plus a fixed-function critical exponent can coexist trivially. The burden is in a **uniform production-and-cancellation certificate** that controls the moving comparator at the same scale where it is used.

This also complements the local-to-global barriers in `MC-001`, `MC-018`, and the Riesz chain. The missing information can be hidden not only in exceptional intervals or a coarse Fourier mode, but in the tail of the arithmetic object itself: any finite observation can be embedded into a globally different multiplicative system whose later values supply an unrelated cancellation theorem.

## 7. Prior art and novelty boundary

Every ingredient is classical.

- NIST DLMF §27.9 records that the Legendre symbol is a Dirichlet character, the supplementary law for `(2/q)`, and quadratic reciprocity: https://dlmf.nist.gov/27.9.
- NIST DLMF §27.11 records Dirichlet's theorem on primes in arithmetic progressions, which supplies a prime in the CRT class: https://dlmf.nist.gov/27.11. The Chinese remainder theorem is catalogued in DLMF §27.15.
- NIST DLMF §25.15 records the Dirichlet `L`-function Euler product and the classical nonvanishing `L(1,chi) != 0` for nonprincipal characters: https://dlmf.nist.gov/25.15.
- Montgomery and Vaughan's classical character-sum literature records the Pólya--Vinogradov bound `max_T |sum_{n<=T} chi(n)| << sqrt(q) log q`; see for example *Mean Values of Character Sums*, Canadian Journal of Mathematics, https://doi.org/10.4153/CJM-1979-035-9.

A targeted search around prescribed finite Legendre-symbol values, quadratic-character prefix interpolation, and Möbius-weighted character sums found these standard mechanisms and neighboring work on prescribed character values, but did not justify any standalone novelty claim for the synthesis above. The result is therefore stored only as a Mathia-specific matched-control obstruction assembled from classical tools.

## 8. Boundary and surviving route

This finding does **not** prove that every scale-dependent comparator strategy is useless. It kills the weaker principle that local agreement plus an independently known fixed-function cancellation exponent is enough.

A surviving comparator mechanism must add information that cannot be manufactured after the observation cutoff. Examples include a conductor-uniform estimate at the operative scale, a global boundary/nonvanishing condition with independently controlled cost, a multiscale relation constraining how the comparator may change as `X` grows, or a signed/bilinear coupling whose estimate is uniform across the moving family.

The decisive audit for future local comparators is now cheap: if the comparator itself depends on `X`, write down the exact constant or norm in its cancellation theorem and evaluate it at the same `X`. If that uniform quantity is lower-bounded by the Mertens target through local agreement, then the construction has only relocated the RH-scale burden.