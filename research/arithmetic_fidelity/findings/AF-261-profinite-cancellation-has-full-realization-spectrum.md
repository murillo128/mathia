# AF-261 — Profinite cancellation has a full realization spectrum

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `DIOPHANTINE-FIDELITY`, `PROFINITE-COVERAGE`, `SHARPNESS`, `NEGATIVE/OBSTRUCTION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-258--AF-260 reduce periodically-complete two-mode Li fidelity to the distribution of the parity-filtered continued-fraction jump rates

\[
\lambda_j:=\frac{2\log q_{j+1}}{q_j}
\qquad(q_j\ \mathrm{even})
\tag{1}
\]

across congruence states of the half-denominators

\[
m_j:=\frac{q_j}{2}.
\tag{2}
\]

The resulting profinite obstruction is not automatically small merely because every finite congruence cylinder must be retained. In fact its entire extended nonnegative range is realizable.

For every

\[
c\in[0,+\infty],
\tag{3}
\]

there exists an irrational number `alpha` whose principal convergents `p_j/q_j` satisfy

\[
\boxed{
K_{M,r}(\alpha)=c
\quad\text{for every }M\ge1\text{ and every }r\bmod M.
}
\tag{4}
\]

Consequently

\[
\boxed{
K_{\mathrm{pc}}(\alpha)=c.
}
\tag{5}
\]

Moreover the same construction can be chosen so that every even principal-convergent denominator belongs to one controlled subsequence on which

\[
\lambda_j\longrightarrow c
\tag{6}
\]

for finite `c`, while `lambda_j -> +infinity` for `c=+infinity`. Hence AF-257 gives simultaneously

\[
\boxed{
\kappa_{1/2}(\alpha)=c.
}
\tag{7}
\]

Thus the general inequality

\[
K_{\mathrm{pc}}(\alpha)\le \kappa_{1/2}(\alpha)
\tag{8}
\]

is sharp at **every** possible level, not only at zero or infinity. AF-258 already exhibits the opposite extreme `kappa_{1/2}=+infinity` with `K_pc=0`; the present result shows that periodic completeness itself supplies no universal positive-margin improvement over the ambient cancellation exponent. Any such improvement for a Keiper phase must use source-specific arithmetic information about that phase.

## Why it matters

AF-260 turns the remaining source problem into a finite-state residue question at each modulus and observes that one weak state, especially one weak `2`-adic shell, is enough to destroy the periodically-complete obstruction. That makes it natural to ask whether the continued-fraction recurrence itself forces some weak shell or weak congruence state.

Equation `(4)` answers that question negatively in the strongest elementary sense. The recurrence can be steered so that the dangerous even-denominator convergents visit **every** finite congruence cylinder infinitely often while their exponential approximation strength is prescribed at one common asymptotic level. No finite modulus, residue, or `2`-adic shell then becomes safer than the ambient channel.

For a hypothetical off-critical Keiper pair with radial factor `q_rho>1`, AF-258 gives the worst periodically-complete pair rate

\[
q_\rho e^{-K_{\mathrm{pc}}(\alpha_\rho)}.
\tag{9}
\]

The realization theorem therefore shows that output coverage alone cannot force this rate to remain above one for arbitrary irrational phases. Given any desired cancellation level `c`, including `c>=log q_rho`, there are irrational phases whose dangerous continued-fraction events recur in every finite congruence cylinder at that level. The missing theorem must distinguish the **actual zero-derived phase** from these engineered controls.

## Exact derivation

### 1. Enumerate every finite congruence requirement recurrently

Choose a sequence

\[
(M_1,r_1),(M_2,r_2),\ldots
\tag{10}
\]

such that every pair

\[
M\ge1,\qquad r\in\mathbb Z/M\mathbb Z
\]

occurs infinitely many times. We construct an infinite simple continued fraction

\[
\alpha=[0;a_1,a_2,a_3,\ldots]
\tag{11}
\]

whose convergent denominators satisfy

\[
q_{-1}=0,\qquad q_0=1,\qquad
q_{j+1}=a_{j+1}q_j+q_{j-1}.
\tag{12}
\]

Start with `a_1=2`, so `q_1=2`. We maintain selected indices

\[
n_0<n_1<n_2<\cdots
\tag{13}
\]

with

\[
n_0=1,
\qquad n_{k+1}=n_k+3,
\tag{14}
\]

such that

\[
q_{n_k}\ \text{is even},
\qquad q_{n_k+1},q_{n_k+2}\ \text{are odd},
\tag{15}
\]

and the next selected half-denominator realizes the next prescribed congruence:

\[
\frac{q_{n_{k+1}}}{2}\equiv r_{k+1}\pmod{M_{k+1}}.
\tag{16}
\]

Because `(15)` leaves no other even denominator between selected indices, this will also identify the complete even-denominator subsequence.

### 2. Tune the exponential jump at each selected even denominator

Assume `q_n` is a selected even denominator and `q_{n-1}` is odd. First choose `a_{n+1}=A_n`.

For finite `c>0`, set

\[
A_n
:=
\left\lceil
\frac{e^{cq_n/2}}{q_n}
\right\rceil.
\tag{17}
\]

Then

\[
e^{cq_n/2}
\le A_nq_n
<e^{cq_n/2}+q_n,
\tag{18}
\]

and therefore

\[
e^{cq_n/2}
<q_{n+1}=A_nq_n+q_{n-1}
<e^{cq_n/2}+2q_n.
\tag{19}
\]

Since `q_n -> infinity`, `(19)` yields

\[
\frac{2\log q_{n+1}}{q_n}\longrightarrow c.
\tag{20}
\]

For `c=0`, take `A_n=1`; then

\[
q_n<q_{n+1}<2q_n,
\]

so the same quotient tends to zero. For `c=+infinity`, choose any sequence `C_k -> +infinity` at the selected stages and replace `c` in `(17)` by `C_k`; then the selected jump rates tend to infinity.

Because `q_n` is even and `q_{n-1}` is odd,

\[
q_{n+1}=A_nq_n+q_{n-1}
\]

is always odd, independently of the size or parity of `A_n`.

### 3. One odd bridge makes the next denominator invertible modulo the target modulus

Let `(M,r)` be the next requirement. We claim that one can choose an **odd** positive integer `b` such that

\[
q_{n+2}:=bq_{n+1}+q_n
\tag{21}
\]

is coprime to `M`.

For each odd prime `p|M`, there are two cases. If `p|q_{n+1}`, then `p` cannot divide `q_n` because consecutive convergent denominators are coprime; hence `(21)` is nonzero modulo `p` for every `b`. If `p` does not divide `q_{n+1}`, exactly one residue class

\[
b\equiv -q_nq_{n+1}^{-1}\pmod p
\tag{22}
\]

would make `(21)` vanish modulo `p`; choose any other class. Together with

\[
b\equiv1\pmod2,
\tag{23}
\]

the Chinese remainder theorem gives a positive odd `b` avoiding all forbidden classes. Thus

\[
\gcd(q_{n+2},M)=1.
\tag{24}
\]

Since `b`, `q_{n+1}` are odd and `q_n` is even, `q_{n+2}` is odd. Hence in fact

\[
\gcd(q_{n+2},2M)=1.
\tag{25}
\]

### 4. The following partial quotient steers the half-denominator into any cylinder

Now choose `a_{n+3}=a` so that

\[
a q_{n+2}+q_{n+1}\equiv2r\pmod{2M}.
\tag{26}
\]

By `(25)`, `q_{n+2}` is invertible modulo `2M`, so the unique residue class is

\[
a
\equiv
(2r-q_{n+1})q_{n+2}^{-1}
\pmod{2M}.
\tag{27}
\]

The right side of `(27)` is odd modulo `2`: `2r-q_{n+1}` is odd and the inverse of the odd number `q_{n+2}` is odd. Choose any positive odd representative `a` of this class. Then

\[
q_{n+3}=a q_{n+2}+q_{n+1}
\tag{28}
\]

is even and, by `(26)`,

\[
\frac{q_{n+3}}2\equiv r\pmod M.
\tag{29}
\]

Equations `(21)` and `(28)` also show that the denominators continue to increase. Thus `(15)`--`(16)` are preserved and the induction can continue forever.

It follows that the complete set of even convergent denominators is precisely

\[
q_{n_0},q_{n_1},q_{n_2},\ldots,
\tag{30}
\]

and their half-denominators visit every congruence cylinder infinitely many times.

### 5. AF-260 makes every cylinder exponent equal to the tuned level

AF-260 proves the exact finite-state identity

\[
K_{M,r}(\alpha)
=
\limsup_{\substack{j\to\infty\\q_j\ \mathrm{even}}}
\frac{\lambda_j}{g_{M,r}(m_j)},
\tag{31}
\]

where `g_{M,r}(m)>=1` is the least odd multiplier carrying `m` to `r mod M`, with an unreachable state contributing zero.

For finite `c`, `(20)` holds along **all** even denominators by `(30)`. Since `g_{M,r}(m_j)>=1`,

\[
K_{M,r}(\alpha)\le c.
\tag{32}
\]

On the other hand, `(10)` and `(29)` provide infinitely many selected indices for which

\[
m_j\equiv r\pmod M.
\tag{33}
\]

At each such index the least transport cost is exactly `g_{M,r}(m_j)=1`. Along that subsequence `lambda_j -> c`, so

\[
K_{M,r}(\alpha)\ge c.
\tag{34}
\]

This proves `(4)` for finite `c`. In the infinite case the same target subsequence has `g=1` and `lambda_j -> +infinity`, so every `K_{M,r}` is infinite as well.

Taking the infimum over all cylinders gives `(5)`. Finally AF-257 identifies

\[
\kappa_{1/2}(\alpha)
=
\limsup_{\substack{j\to\infty\\q_j\ \mathrm{even}}}
\lambda_j,
\tag{35}
\]

which is exactly `c` by construction, proving `(7)`.

## Prior-art audit

Congruence behavior of continued-fraction convergents is classical and substantially stronger distribution theorems are known in metric settings. Bence Borda, **“Equidistribution of continued fraction convergents in `SL(2,Z_m)` with an application to local discrepancy,”** *Journal of Modern Dynamics* 21 (2025), 327–359, DOI `10.3934/jmd.2025005`, studies the full consecutive-convergent matrix modulo a fixed modulus and proves refined limit laws, building on earlier strong-law work of Szüsz, Moeckel, Jager, and Liardet. In particular, modular recurrence of convergent denominators is not new structure here.

Direct older references include R. Moeckel, **“Geodesics on modular surfaces and continued fractions,”** *Ergodic Theory and Dynamical Systems* 2 (1982), 69–83, DOI `10.1017/S0143385700009585`, and H. Jager and P. Liardet, **“Distributions arithmétiques des dénominateurs de convergents de fractions continues,”** *Indagationes Mathematicae* 50 (1988), 181–197, DOI `10.1016/S1385-7258(88)80026-X`. Congruence-constrained Diophantine approximation more generally is also established prior art, including E. Nesharim, R. Rühr, and R. Shi, **“Metric Diophantine approximation with congruence conditions,”** *International Journal of Number Theory* 16 (2020), 1923–1933, DOI `10.1142/S1793042120500980`.

Large partial quotients and prescribed exceptional approximation rates likewise belong to classical and modern metric Diophantine approximation. AF-257 already audits the unrestricted exponential scale against Sondow's irrationality-base formalism and the parity-restricted approximation literature.

The present proof does not claim novelty for the continued-fraction recurrence, modular steering, prime avoidance, Chinese remaindering, or the existence of irrationals with engineered large partial quotients. A targeted search located extensive literature on modular distribution of convergents and on large partial quotients, but did not locate the exact joint realization statement `(4)`: simultaneous recurrent coverage of every finite half-denominator cylinder while fixing the AF-258/AF-260 exponential cancellation level in every cylinder. This is not an exhaustive novelty proof. The durable contribution is the sharpness consequence for the already-defined Arithmetic Fidelity invariant.

## Boundaries and falsification checks

**Engineered phases, not zeta phases.** The construction proves that continued-fraction recurrence plus periodic-complete output coverage cannot by themselves force a safe cylinder. It says nothing about whether a phase derived from an actual Riemann zero can realize these engineered partial quotients.

**Two-mode dominant-pair regime.** The quantities `K_{M,r}` and `K_pc` here are the scalar half-integer cancellation invariants of AF-258--AF-260. Multi-mode cancellation is governed by the fiber-norm framework of AF-246/AF-253 and need not reduce to one continued fraction.

**No contradiction with typical modular equidistribution.** The construction deliberately correlates exceptionally large partial quotients with prescribed modular states. Metric equidistribution theorems for almost every irrational do not preclude exceptional explicitly engineered irrationals.

**The common level is essential to the sharpness statement, not a classification of all possible profiles.** The proof realizes constant cylinder profiles `K_{M,r}=c`. It does not classify which nonconstant families of cylinder exponents can arise from one irrational phase.

**The bridge step really needs only finite prime avoidance.** If the claim were false, the vulnerable point would be the assertion that an odd `b` can make `(21)` coprime to arbitrary `M`. For each prime divisor of `M` there is at most one forbidden residue when `q_{n+1}` is invertible, and no forbidden residue when it is not; CRT therefore supplies the required odd `b`. This is independent of the jump-tuning choice `A_n`.

## Research consequence

AF-260's shell criterion is a potentially useful **source theorem**, but it cannot be upgraded into a universal theorem about irrational phases. Even the strongest finite-coverage contract considered so far admits phases for which every cylinder and every exact `2`-adic shell carries the full ambient exponential cancellation level.

The live RH-facing question therefore narrows further. To prove periodically-complete Li root-rate fidelity for an actual Keiper phase, one must establish arithmetic information tied to the zero coordinate itself—for example a weak congruence/`2`-adic shell below the radial margin, or another source-specific restriction on the correlation between enormous continued-fraction jumps and the half-denominator residue itinerary. Pure continued-fraction recurrence and output coverage are now known to be insufficient.