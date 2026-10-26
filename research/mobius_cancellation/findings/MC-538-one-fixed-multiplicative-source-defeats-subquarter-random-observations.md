# MC-538 — One fixed multiplicative source defeats subquarter random observations

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`,
`MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`. This is a comparator theorem,
not a lower bound for Möbius or a new estimate for its summatory function.

## Claim and order of choices

Fix a nonzero complex function \(\phi\in C_c^1((4/3,5/3))\), an
observation exponent \(0\le\alpha<1/4\), and
\[
                 3/4<\kappa<1-\alpha.
\tag{1}
\]
There exist one deterministic multiplicative function
\[
 f:\mathbb N\longrightarrow\{-1,0,1\},\qquad |f(n)|=\mu(n)^2,
\tag{2}
\]
and one deterministic increasing sequence of integer scales
\(X_k\to\infty\) with the following properties. Set
\[
 F(y)=\sum_{n\le y}f(n),\quad S_L(j)=F(j+L)-F(j),\qquad
 L_1(X)=\lfloor X/20\rfloor,\quad
 L_2(X)=\lfloor\sqrt2 L_1(X)\rfloor.
\tag{3}
\]
At every selected scale,
\[
 \boxed{\left|\sum_n f(n)\phi(n/X_k)\right|
        \gg_\phi \frac{X_k^{2\kappa-1}}{(\log X_k)^2}.}
\tag{4}
\]
Both \(f\) and the entire scale sequence are fixed **before** any
observation locations are drawn. At each integer scale \(X\), draw
\(2q_X=2\lceil X^\alpha\rceil\) independent uniform starts per
channel from \(I_X=\{X,\ldots,2X-1\}\), with replacement, and put
\[
 E_i(X)=\frac1{2q_X}\sum_{a=1}^{2q_X}
               |S_{L_i(X)}(R_{i,X,a})|^2.
\tag{5}
\]
Under the product sampling law, almost surely, on that same fixed
scale sequence and for every \(\varepsilon>0\),
\[
 \boxed{E_i(X_k)\ll_\varepsilon X_k^{1+\varepsilon}
                         \quad(i=1,2).}
\tag{6}
\]
Consequently the centered sample variances also satisfy (6). Repeated
draws retain their multiplicities. The constant and eventual onset in
(6) may depend on the sampling outcome; the function and scales do not.

Since \(2\kappa-1>1/2\), (4) has a fixed power excess over the
square-root scale. In particular this fixed \(f\) cannot satisfy
\(F(y)\ll_\varepsilon y^{1/2+\varepsilon}\) for every epsilon:
summation by parts would give the same bound for the left side of (4).

[MC-535](MC-535-multiplicative-prime-bridges-retain-sparse-window-ambiguity.md)
chooses multiplicative controls after fixing the observed starts at one
scale. [MC-537](MC-537-small-sampled-energy-permits-quarter-power-mobius-observations.md)
gives a smaller-exponent obstruction for bounded-jump signal families,
but those tents are not common multiplicative coefficient realizations.
The present result removes both restrictions for the stated sampling
law. It uses the lacunary conditioning mechanism already present in
[MC-120](MC-120-fixed-function-lacunary-fractional-moment-barrier.md),
with a signed smooth target and two sampled window energies replacing
that finding's fractional moments. No dense-scale conclusion is claimed.

## 1. A narrow balanced prime block from the ordinary PNT

Choose a closed interval \([s,t]\Subset(4/3,5/3)\), a unit complex
number \(\omega\), and \(\eta>0\) such that
\[
       \operatorname{Re}(-\omega\phi'(u))\ge\eta
                                      \quad(s\le u\le t).
\tag{7}
\]
Such an interval exists since a nonzero compactly supported function
cannot have identically zero derivative. At a large integer scale \(X\),
put \(A=\lfloor X^\kappa\rfloor\). Partition
\((\lceil sX\rceil,\lfloor tX\rfloor]\) into consecutive integer
cells of length at most \(A\). There are \(O_\phi(X/A)\) cells.
The prime number theorem gives \(\gg_\phi X/\log X\) primes in
their union, so at least one cell \((a,b]\) contains
\[
                       m\gg_\phi A/\log X
\tag{8}
\]
primes. This is an existence statement about one cell; no prime
asymptotic in every interval of length \(A\) is used.

Take \(2h=2\lfloor m/2\rfloor\) of its primes in increasing order
\(p_1<\cdots<p_{2h}\). Prescribe signs \(b_{p_\ell}=+1\) for
\(\ell\le h\) and \(-1\) for \(\ell>h\). Their primitive
\[
                     B(y)=\sum_{p_\ell\le y}b_{p_\ell}
\tag{9}
\]
is nonnegative, zero outside \([a,b]\), and exactly balanced. At
\(p_\ell\) it equals \(\min(\ell,2h-\ell)\). Merely retaining
these distinct integer positions gives
\[
                       \sum_{n=a}^{b-1} B(n)\ge h^2.
\tag{10}
\]
Discrete summation by parts therefore shows that the block contribution
\(T_B(X)=\sum_\ell b_{p_\ell}\phi(p_\ell/X)\) satisfies
\[
 \operatorname{Re}(\omega T_B(X))
 =-\sum_{n=a}^{b-1}B(n)\operatorname{Re}
          \bigl(\omega[\phi((n+1)/X)-\phi(n/X)]\bigr)
 \ge\frac{\eta h^2}{X}
 \ge G(X):=c_\phi\frac{X^{2\kappa-1}}{(\log X)^2}
\tag{11}
\]
for a fixed \(c_\phi>0\) and all sufficiently large \(X\).

For the observation horizon \(N_X=2X-1+L_2(X)\),
\[
                        N_X<2\min_\ell p_\ell.
\tag{12}
\]
Thus changing these prime signs affects only the primes themselves
below \(N_X\), not any composite coefficient. This also covers the
support of the smooth target, which is below \(5X/3\).

## 2. Earlier prescribed signs cost a finite second-moment factor

Choose separated scales \(X_k\) and one block \(P_k\) as above at
each scale. Require \(X_{k+1}>3X_k\); hence every future block lies
above \(N_{X_k}\). These choices are made before random prime signs.
Let
\[
 A_{<k}=\bigcup_{r<k}P_r,\quad r_k=|A_{<k}|,\quad C_k=2^{r_k}.
\tag{13}
\]
Prescribe the balanced signs at every prime in \(\bigcup_kP_k\).
At all remaining primes assign independent Rademacher signs. Set every
prime-power value of exponent at least two to zero, and extend
multiplicatively. This defines a random function with (2) exactly.

For stage \(k\), let \(g_k\) be the auxiliary multiplicative function
obtained by setting its current-block prime values to zero. For any
complex weights \(v_n\) supported on \(1\le n\le N_{X_k}\),
\[
 \boxed{\mathbb E\left|\sum_n v_ng_k(n)\right|^2
                            \le C_k\sum_n|v_n|^2.}
\tag{14}
\]
To prove it, restrict to square-free integers avoiding \(P_k\), and
write each uniquely as \(n=dm\), where \(d\) uses only primes in
\(A_{<k}\) and \(m\) uses none. No future prescribed prime occurs.
If \(b_d\in\{-1,1\}\) is the old prescribed product, group by
\(m\):
\[
 \sum_n v_ng_k(n)=\sum_m\epsilon(m)
                   \sum_{d\mid\prod_{p\in A_{<k}}p} b_dv_{dm}.
\tag{15}
\]
Only the admissible square-free pairs avoiding \(P_k\) are included
in these sums, and weights outside the horizon are zero. Distinct
\(m\) give orthogonal Rademacher monomials, including the constant
monomial \(m=1\). Squaring and applying Cauchy--Schwarz to the at
most \(C_k\) terms in each inner sum proves (14); uniqueness of
\(n=dm\) counts each remaining \(|v_n|^2\) at most once.

This estimate includes all composite copies of old prime blocks.
It does not assert independence of interval sums or condition on
previously successful random stage events.

Define the complete two-channel background energy
\[
 U_k=\sum_{i=1}^2\frac1{X_k}
       \sum_{j=X_k}^{2X_k-1}
       \left|\sum_{j<n\le j+L_i(X_k)}g_k(n)\right|^2.
\tag{16}
\]
Equation (14) gives
\[
 \mathbb E U_k\le C_k(L_1(X_k)+L_2(X_k))\le C_kX_k,
 \qquad
 \mathbb E|T_{g_k}(X_k)|^2\le K_\phi C_kX_k,
\tag{17}
\]
where \(T_{g_k}(X)=\sum_n g_k(n)\phi(n/X)\) and \(K_\phi\)
is a fixed bound for \(X^{-1}\sum_n|\phi(n/X)|^2\).

## 3. Fix one global coefficient sequence before observing it

Put \(\delta_k=2^{-k-4}\). At stage \(k\), \(C_k\) is already
determined by the previous deterministic blocks. Choose \(X_k\)
large enough for (8)--(12), separation from the preceding scale, and
\[
 X_k\ge2^{k^2},\qquad
 C_k/\delta_k\le X_k^{1/k},\qquad
 \frac{4K_\phi C_kX_k}{G(X_k)^2}\le\delta_k.
\tag{18}
\]
All are possible: the last ratio is a constant times
\(C_kX_k^{3-4\kappa}(\log X_k)^4\), which tends to zero since
\(\kappa>3/4\). Then choose the current prime cell and signs.
This completes the deterministic scale/block sequence; only afterward
are the other prime signs randomized.

By Markov's inequality and (17), the probability that either
\[
              U_k\le X_k^{1+1/k},\qquad
              |T_{g_k}(X_k)|\le G(X_k)/2
\tag{19}
\]
fails is at most \(2\delta_k\). Since
\(\sum_{k\ge1}2\delta_k<1\), the countable union bound supplies
one global sign assignment for which (19) holds at **every** stage.
Fix that assignment once and for all. The resulting \(f\) is now
deterministic. No observation locations have been drawn.

Within the stage horizon, (12) gives the exact identity
\[
                 F(y)=G_k(y)+B_k(y),\qquad
                 G_k(y)=\sum_{n\le y}g_k(n).
\tag{20}
\]
In particular \(T_f(X_k)=T_{g_k}(X_k)+T_{B_k}(X_k)\).
Equations (11) and (19) prove (4), with constant \(c_\phi/2\).
Earlier block replicas are already inside \(g_k\); future prime
assignments cannot change any coefficient in this stage's horizon.

## 4. Sparse random starts miss the current bridge almost surely

For the fixed function and scales above, the only starts where
\(S_{L_i,f}\) can differ from \(S_{L_i,g_k}\) have at least one
endpoint \(j,j+L_i\) inside \([a_k,b_k]\). There are at most
\(2(A_k+1)\) such starts in each channel. For \(2q_{X_k}\)
observations per channel, the union bound gives
\[
 \Pr\{\text{some sampled endpoint meets }[a_k,b_k]\}
 \le\frac{8q_{X_k}(A_k+1)}{X_k}
 \ll X_k^{\alpha+\kappa-1}.
\tag{21}
\]
These probabilities are summable by (1) and (18).

Also, by the first inequality in (19), the expected sample average
of \(|S_{L_i,g_k}|^2\) is at most \(X_k^{1+1/k}\).
Markov's inequality bounds the probability that this sample average
exceeds \(X_k^{1+2/k}\) by
\[
                          X_k^{-1/k}\le2^{-k}.
\tag{22}
\]
Apply the first Borel--Cantelli lemma to (21) and both channels of
(22). Almost surely, for every sufficiently large \(k\), no sampled
endpoint hits the current bridge and both sampled background energies
are at most \(X_k^{1+2/k}\). On that event (20) identifies every
observed interval sum with its background value. Therefore
\[
                         E_i(X_k)\le X_k^{1+2/k}
\tag{23}
\]
eventually, simultaneously for \(i=1,2\). This single event implies
(6) for every epsilon; there is no epsilon-dependent scale selection.
The elementary inequality \(\min_c\sum|Y_a-c|^2\le\sum|Y_a|^2\)
gives the centered version. Independence across scales is not needed
for this last step, though the specified product law provides it.

## Prior art, controls and significance

The only prime-supply input is the ordinary PNT
([NIST DLMF, §27.12](https://dlmf.nist.gov/27.12), MC-S89).
Pigeonholing its fixed-proportion interval count gives one narrow cell;
the logarithm is squared because (10) retains only prime positions.
No uniform short-interval prime theorem or optimal logarithm is claimed.
The Rademacher multiplicative model is classical
([Harper, Section 1](https://msp.org/ant/2019/13-10/ant-v13-n10-p02-s.pdf),
MC-S88). Its high-moment estimates are not used: (14) proves the
finite-prescription bound needed here. MC-120 already supplies the
line's one-function lacunary conditioning strategy. MC-535 supplies
the isolated-prime bridge with a signed target. Their different
conclusions are not silently upgraded; Sections 2--4 establish the
new common-source/random-observation quantifiers.

Hidden-area sampling obstructions are classical in
[Baran--Demaine--Katz](https://erikdemaine.org/papers/Integration_Algorithmica/paper.pdf)
(MC-S85). The square-free multiplicative discrepancy class is also
established in [Klurman--Mangerel--Pohoata--Teräväinen](https://arxiv.org/abs/1911.06265)
(MC-S16); unbounded discrepancy alone does not provide (4)--(6).
A structural literature check of prescribed-prime random models,
multiplicative discrepancy, and randomized Lipschitz integration
supports these ingredients, not an external novelty claim for their
assembly.

The mathematical delta is a fixed-source obstruction to a particular
proposed improvement of the observation interface. Below the
quarter-power sample exponent, **one fixed multiplicative function
with exact square-free support** can have RH-scale sampled energies
in both macroscopic channels, almost surely on a predetermined
unbounded sequence, while a fixed signed smooth target has a larger
power. Source adaptation to the samples, changing the source at each
scale, and nonmultiplicative tents are unnecessary for this obstruction.

Its boundaries are essential:

- The scales may be extremely far apart. The finite factor \(C_k\)
  is paid by that freedom; no dense-scale or all-scale energy ceiling
  is constructed.
- The signs at selected primes include \(+1\), so the source is not
  Möbius and does not retain \(\mu(p)=-1\) or \(1/\zeta\).
  No quantitative Chowla or other Möbius-specific constraints are imposed.
- The sampling guarantee concerns the stated uniform law and the
  sampled energy, not arbitrary adaptive designs, every seed, or exact
  indistinguishability from one second fixed source. The current
  auxiliary \(g_k\) is allowed to vary with \(k\); the observed
  source \(f\) is not.
- Nothing is disproved at exponent \(1/4\), and nothing contradicts
  MC-537's quarter-power recovery theorem. A smaller-exponent theorem
  specifically for Möbius would need additional arithmetic input.
- This gives neither a reciprocal-zeta pole nor any RH consequence.
  Large comparator sums do not transfer to the actual Möbius function.

Exact finite checks enumerated 512 assignments with old primes
\(\{2,3,5\}\), current block \(\{29,31,37,41\}\), and horizon
41. They verified 336 weighted second-moment identities and their
finite-prescription bounds, 20,992 exact prefix identities, 64,000
coprime-product identities, and 6,656 interval equalities away from
the bridge. A further 2,509 even blocks with arbitrary distinct
integer positions verified nonnegativity, the \(h^2\) area bound,
and signed summation by parts. These bookkeeping checks do not prove
the PNT, the infinite probabilistic construction, or a Möbius estimate;
the arguments above establish the stated theorem. No Lean validation
or independent adversarial approval is asserted. Its elementary
finite-moment component does not currently expose a separate
high-value formalization target.
