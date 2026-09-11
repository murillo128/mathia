# AF-260 — Fixed congruence cylinders reduce to finite odd-transport states

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `DIOPHANTINE-FIDELITY`, `PROFINITE-COVERAGE`, `FINITE-STATE-REDUCTION`, `LI-DOMINANT-MODE-CONTROL`, `CANDIDATE-NEW-STRUCTURE`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-259 expresses each congruence-cylinder cancellation exponent through even principal-convergent denominators and arbitrary odd transport multipliers. For a **fixed** cylinder, that multiplier quantifier can be eliminated completely.

Let

\[
\alpha=[a_0;a_1,a_2,\ldots],
\qquad \frac{p_j}{q_j}
\]

be the principal convergents of an irrational `alpha`. On the subsequence with `q_j` even, put

\[
m_j:=\frac{q_j}{2},
\qquad
\lambda_j:=\frac{2\log q_{j+1}}{q_j}.
\tag{1}
\]

For a modulus `M>=1`, residue `r mod M`, and integer `m>=1`, define the **least odd transport cost**

\[
g_{M,r}(m)
:=
\min\{g\ge1:\ g\ \text{odd},\ gm\equiv r\pmod M\},
\tag{2}
\]

with `g_{M,r}(m)=infinity` when no such odd multiplier exists, and use `1/infinity=0`.

Then the AF-258 cylinder exponent has the exact finite-state form

\[
\boxed{
K_{M,r}(\alpha)
=
\limsup_{\substack{j\to\infty\\q_j\ \mathrm{even}}}
\frac{\lambda_j}{g_{M,r}(m_j)}.
}
\tag{3}
\]

The cost `g_{M,r}(m)` depends only on `m mod M`. Hence for each fixed `(M,r)` there is a finite weight table

\[
c_{M,r}(u):=\frac1{g_{M,r}(u)},
\qquad u\in\mathbb Z/M\mathbb Z,
\tag{4}
\]

such that

\[
\boxed{
K_{M,r}(\alpha)
=
\limsup_{\substack{j\to\infty\\q_j\ \mathrm{even}}}
\lambda_j\,c_{M,r}(m_j\bmod M).
}
\tag{5}
\]

Consequently the full profinite exponent is

\[
\boxed{
K_{\mathrm{pc}}(\alpha)
=
\inf_{M\ge1}\min_{r\bmod M}
\limsup_{\substack{j\to\infty\\q_j\ \mathrm{even}}}
\lambda_j\,c_{M,r}(m_j\bmod M).
}
\tag{6}
\]

Thus AF-259's odd-multiplier leakage problem is, cylinder by cylinder, a **weighted finite-state residue process**. No boundedness assumption on the jump rates `lambda_j` is needed to make the multiplier optimization finite once the cylinder is fixed.

The transport table is elementary and explicit. Let

\[
d=\gcd(m,M),
\qquad M_0=\frac Md.
\tag{7}
\]

If `d` does not divide `r`, then `g_{M,r}(m)=infinity`. If `d|r`, write

\[
m_0=\frac md,
\qquad r_0=\frac rd,
\qquad \gcd(m_0,M_0)=1.
\tag{8}
\]

When `M_0` is even, an odd transport exists exactly when `r_0` is odd; in that case `g_{M,r}(m)` is the least positive residue of

\[
r_0m_0^{-1}\pmod{M_0},
\tag{9}
\]

which is automatically odd. When `M_0` is odd, an odd representative always exists. In every reachable state,

\[
\boxed{g_{M,r}(m)<2M_0\le2M.}
\tag{10}
\]

The prime `2` is structurally special because the transport multipliers themselves are odd. They cannot change the `2`-adic valuation of `m_j`. Define the exact shell rates

\[
L_t(\alpha)
:=
\limsup_{\substack{j\to\infty\\q_j\ \mathrm{even}\\v_2(m_j)=t}}
\lambda_j,
\qquad t\ge0,
\tag{11}
\]

with value `0` when the indexing set is finite. Then

\[
\boxed{
K_{2^{t+1},\,2^t}(\alpha)=L_t(\alpha).
}
\tag{12}
\]

Likewise, with

\[
L_{\ge a}(\alpha)
:=
\limsup_{\substack{j\to\infty\\q_j\ \mathrm{even}\\v_2(m_j)\ge a}}
\lambda_j,
\tag{13}
\]

one has

\[
\boxed{
K_{2^a,0}(\alpha)=L_{\ge a}(\alpha).
}
\tag{14}
\]

Therefore

\[
\boxed{
K_{\mathrm{pc}}(\alpha)
\le
\inf_{t\ge0}L_t(\alpha),
}
\tag{15}
\]

and also `K_pc(alpha)<=L_{>=a}(alpha)` for every `a>=1`.

This gives a sharp new necessary condition for persistent periodically-complete cancellation. If

\[
K_{\mathrm{pc}}(\alpha)\ge c>0,
\tag{16}
\]

then **every exact `2`-adic shell** of the half-denominators must carry jump rate at least `c`:

\[
\boxed{L_t(\alpha)\ge c\quad\text{for every }t\ge0.}
\tag{17}
\]

A single weak shell kills the obstruction. In particular, if `L_t(alpha)=0` for any `t`, then `K_pc(alpha)=0` even when the unrestricted AF-257 exponent is positive or infinite.

## Why it matters

AF-259 leaves the source theorem in a form that still appears to involve two unbounded resources: the continued-fraction index `j` and the odd multiplier `g`. It observes that a fixed positive detectability margin restricts `g` when the parity-filtered jump rates are bounded, but explicitly notes that no such bounded-jump hypothesis is known for a Keiper phase.

Equation `(3)` removes that apparent obstacle at fixed modulus. For one cylinder, the best contribution of a given principal convergent always uses the **smallest** admissible odd multiplier, and elementary congruence theory bounds that multiplier by `2M`. Large odd multipliers are never competitive. The remaining difficulty is therefore entirely in the weighted residue itinerary of the half-denominators `m_j` and the jump sizes `lambda_j`.

The `2`-adic specialization is stronger still. For the cylinder

\[
n\equiv2^t\pmod{2^{t+1}},
\]

positive exponential cancellation can come only from convergents with

\[
v_2(q_j/2)=t.
\]

Moreover `g=1` already places every such half-denominator in that cylinder, so there is no multiplier loss at all. Thus a hypothetical obstruction that survives **every** periodically complete sampler must reproduce sufficiently large continued-fraction jumps separately in every `2`-adic valuation shell.

This reframes the live source problem after AF-259. It is no longer necessary first to prove a global irrationality-base bound or a global bound on `lambda_j`. One may instead try to find a single finite residue state, and in particular a single exact `2`-adic shell, on which the dangerous jumps fall below the zero-dependent radial margin.

## Exact derivation

### 1. For one convergent, the least admissible odd multiplier is optimal

AF-259 gives

\[
K_{M,r}(\alpha)
=
2\limsup_{\substack{q_j\ \mathrm{even},\ g\ \mathrm{odd}\\
gm_j\equiv r\ (M)}}
\frac{[\log(q_{j+1}/g)]_+}{gq_j}.
\tag{18}
\]

For fixed `j`, write `Q=q_{j+1}` and consider

\[
f_Q(g)=\frac{[\log(Q/g)]_+}{g},
\qquad g\ge1.
\tag{19}
\]

On `1<=g<Q`,

\[
f_Q'(g)
=-\frac{1+\log(Q/g)}{g^2}<0,
\tag{20}
\]

and for `g>=Q` the positive part makes `f_Q(g)=0`. Hence among all admissible odd multipliers for a fixed `j`, the contribution in `(18)` is maximized by `g_{M,r}(m_j)`.

If no admissible odd multiplier exists, that convergent contributes zero to the positive exponential limsup. Therefore `(18)` becomes

\[
K_{M,r}(\alpha)
=
\limsup_{\substack{j\to\infty\\q_j\ \mathrm{even}}}
\frac{2}{g_jq_j}
[\log(q_{j+1}/g_j)]_+,
\tag{21}
\]

where `g_j=g_{M,r}(m_j)` and an unreachable state contributes zero.

### 2. Odd congruence transport is a finite table

The congruence

\[
gm\equiv r\pmod M
\tag{22}
\]

has an integer solution only if `d=gcd(m,M)` divides `r`. After dividing by `d`, it becomes

\[
gm_0\equiv r_0\pmod{M_0},
\qquad \gcd(m_0,M_0)=1,
\tag{23}
\]

so every solution lies in the unique residue class

\[
g\equiv r_0m_0^{-1}\pmod{M_0}.
\tag{24}
\]

If `M_0` is even, adding multiples of `M_0` cannot change parity. Since `m_0` is then odd, the residue in `(24)` is odd exactly when `r_0` is odd. This proves the even-`M_0` reachability criterion.

If `M_0` is odd, adding one copy of `M_0` flips parity. Hence every residue class modulo `M_0` has a positive odd representative. Choosing the least one gives a value below `2M_0`; in the even case the least positive representative is already odd and below `M_0`. This proves `(10)`.

In particular, for fixed `M`, every finite transport cost satisfies

\[
1\le g_j<2M.
\tag{25}
\]

Since `q_{j+1}->infinity`, the positive part in `(21)` is eventually inactive on every reachable subsequence with `j->infinity`. Moreover

\[
\frac{2}{g_jq_j}\log\frac{q_{j+1}}{g_j}
=
\frac{\lambda_j}{g_j}
-
\frac{2\log g_j}{g_jq_j}.
\tag{26}
\]

The second term is uniformly `O_M(1/q_j)` by `(25)`, hence tends to zero. This proves `(3)`. Because `g_{M,r}(m)` depends only on the residue of `m` modulo `M`, equations `(5)` and `(6)` follow.

The reduction is exact at the level of the limsup exponent. It does not assert that every individual small-cancellation sample uses a bounded multiplier; rather, all larger admissible multipliers are dominated by the least one when computing the cylinder's asymptotic exponential rate.

### 3. Powers of two isolate exact valuation shells

Take

\[
M=2^{t+1},
\qquad r=2^t.
\tag{27}
\]

Because `g` is odd,

\[
v_2(gm)=v_2(m).
\tag{28}
\]

Thus `(22)` can hold only when `v_2(m)=t`. Conversely, if `v_2(m)=t`, write `m=2^tu` with `u` odd. Then

\[
m\equiv2^t\pmod{2^{t+1}},
\tag{29}
\]

so `g=1` is already admissible and is necessarily the least transport cost. Equation `(3)` therefore becomes exactly `(12)`.

For `M=2^a` and `r=0`, odd multiplication cannot add a missing factor of two. Hence the zero cylinder is reachable exactly when `2^a|m`, again with least cost `g=1`. This proves `(14)`.

Finally `K_pc` is the infimum over all cylinders, so `(12)` immediately gives `(15)`. If `(16)` held while some `L_t<c`, then the single cylinder `(2^{t+1},2^t)` would have exponent below `c`, contradicting the definition of `K_pc`. This proves `(17)`.

## Keiper-pair consequence

For the hypothetical off-critical zero notation of AF-255--AF-259,

\[
a_\rho=r_\rho e^{i\theta_\rho},
\qquad
q_\rho=r_\rho^{-1}>1,
\qquad
\alpha_\rho=\frac{\theta_\rho}{\pi},
\tag{30}
\]

AF-258 says that every periodically complete sampler preserves a uniform strictly superunit pair rate exactly when

\[
K_{\mathrm{pc}}(\alpha_\rho)<\log q_\rho.
\tag{31}
\]

AF-260 yields the clean sufficient condition

\[
\boxed{
\exists t\ge0:\quad
L_t(\alpha_\rho)<\log q_\rho
\quad\Longrightarrow\quad
K_{\mathrm{pc}}(\alpha_\rho)<\log q_\rho.
}
\tag{32}
\]

The stronger condition `L_t(alpha_rho)=0` for one shell forces full pair-rate fidelity. Alternatively, for any `a>=1`,

\[
L_{\ge a}(\alpha_\rho)<\log q_\rho
\tag{33}
\]

is sufficient by `(14)`.

Conversely, any hypothetical pair that can be suppressed to unit root rate or below by a periodically complete retained set must satisfy the necessary shell-recurrence condition

\[
\boxed{
L_t(\alpha_\rho)\ge\log q_\rho
\qquad\text{for every }t\ge0.
}
\tag{34}
\]

At large zero height the margin `log q_rho` is tiny, of order `(beta-1/2)/gamma^2` by AF-255, so `(34)` is still far from a contradiction. But it is qualitatively much stronger than the ambient AF-257 requirement: dangerous parity-selected continued-fraction jumps cannot merely occur infinitely often; they must recur above the radial margin in **every exact `2`-adic shell** of `q_j/2`.

Equation `(6)` gives the sharper route when powers of two are insufficient. For any candidate finite modulus `M`, one needs only the finite table `c_{M,r}` and the residue sequence `m_j mod M`; no search over unbounded odd multipliers remains.

## Prior-art audit

The ingredients used to derive `(3)` are classical: principal continued fractions, linear congruences, parity, and the monotonicity of `log(Q/g)/g`. AF-257 and AF-259 already audit the approximation step against Dong Han Kim, Seul Bee Lee, and Lingmin Liao, **“Diophantine approximation by rational numbers of certain parity types,”** *Mathematika* 71(1) (2025), e12285, DOI `10.1112/mtk.12285`, and against R. T. Worley, **“Restricted diophantine approximation,”** *Journal of the Australian Mathematical Society* 24(4) (1977), 425–439, DOI `10.1017/S1446788700020802`.

Residue statistics of continued-fraction convergents are also established mathematics. Bence Borda, **“Equidistribution of continued fraction convergents in SL(2,Z_m) with an application to local discrepancy,”** *Journal of Modern Dynamics* 21 (2025), 327–359, DOI `10.3934/jmd.2025005`, studies the distribution of `p_n mod m`, `q_n mod m`, and the full consecutive-convergent matrix modulo a fixed modulus for typical irrational inputs. Earlier arithmetic work on convergents includes P. Erdős and K. Mahler, **“Some Arithmetical Properties of the Convergents of a Continued Fraction,”** *Journal of the London Mathematical Society* s1-14(1) (1939), 12–18, DOI `10.1112/jlms/s1-14.1.12`.

These sources make clear that congruence classes of convergents, parity-restricted approximation, and modular continued-fraction dynamics are not new. A targeted search did not locate the exact weighted identity `(3)`--`(6)` for the AF-258 half-integer exponential observable, nor the exact shell identity `(12)` connecting its profinite minimax exponent to `2`-adic valuations of the half-denominators. This is not an exhaustive novelty proof. The narrow `CANDIDATE-NEW-STRUCTURE` content is the removal of AF-259's unbounded multiplier variable by a finite odd-transport cost table and the resulting `2`-adic shell gate for periodically-complete Li cancellation.

## Boundaries and falsification

**This is still a two-mode theorem.** The odd transport law originates in reduction of approximation to the half-integer zero set of one conjugate cosine pair. A multimode zero fiber can have different arithmetic and need not inherit the same finite-state table.

**Finite-state does not mean globally finite.** For each fixed modulus there are only finitely many transport states and the optimal multiplier is bounded by `2M`, but `K_pc` still takes an infimum over arbitrarily large moduli. AF-260 does not reduce the entire profinite problem to one universal finite automaton.

**The `2`-adic condition is sufficient, not a classification.** Equation `(15)` can be strict because odd-modulus or finer mixed-modulus cylinders may have substantially smaller weighted leakage than every pure `2`-adic shell. The exact invariant is `(6)`.

**No zeta-zero theorem is inserted.** Nothing here proves that an actual hypothetical Keiper phase has one weak `2`-adic shell, nor that its convergent denominators are equidistributed modulo powers of two. Typical-irrational equidistribution results cannot be applied to a specific zeta-derived phase without an independent source theorem.

**No bounded-jump hypothesis is used.** The bounded transport in `(25)` comes from fixing the congruence cylinder, not from bounding `lambda_j`. A counterexample to `(3)` would therefore require a fixed `(M,r)` and a sequence whose best exponential contribution comes from an odd multiplier larger than the least congruence solution; monotonicity `(20)` rules this out.

## Consequence

The source-specific obstruction after AF-259 is now a finite-state weighted recurrence problem. For a hypothetical off-critical Keiper phase, failure of periodically-complete fidelity at margin `log q_rho` requires its exponentially large even-denominator continued-fraction jumps to remain above that margin in every exact `2`-adic shell, and more generally to defeat every finite odd-transport table `(M,r)`.

This does not solve the source theorem, but it materially narrows its form. A future attack may work on one residue shell at a time; it does not need to control arbitrary odd multiples or prove a global irrationality-base estimate before obtaining a useful fidelity certificate.