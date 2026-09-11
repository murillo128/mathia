# VIS-163 — a held-out prime phase has no continuous decoder from finite prime support

## Claim

Let `P={p_1,...,p_k}` be a finite set of at least two distinct rational primes, let `r` be a prime not in `P`, and define

`Phi_P(t)=(p_1^(-it),...,p_k^(-it)) in T^k`,

`A_r(t)=r^(-it) in T`.

Then the held-out prime phase `A_r` is set-theoretically determined by `Phi_P(t)` because `Phi_P` is injective, but it is **not continuously recoverable** from the finite prime torus. More precisely:

1. there is no continuous `F:T^k->C` satisfying `F(Phi_P(t))=A_r(t)` for every real `t`;
2. the induced orbit decoder `f(Phi_P(t))=A_r(t)` on the dense orbit `Phi_P(R)` is nowhere continuous;
3. its Lipschitz collision quotient is infinite,

`Lambda_P(A_r;R)=sup_(t!=u) |A_r(t)-A_r(u)|/||Phi_P(t)-Phi_P(u)||_2 = infinity`;

4. for every finite `T`, `Lambda_P(A_r;[-T,T])<infinity`, but these finite-window constants diverge as `T->infinity`.

Thus failure of continuous or Lipschitz decoding from a **fixed finite prime support** is not by itself a zeta-specific or zero-side signal. A single omitted prime frequency already has that failure exactly.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-KRONECKER-WEYL-SPECIALIZATION + REPRESENTATION-OBSTRUCTION + DECISIVE-NEGATIVE-CONTROL + NO-NOVELTY-CLAIM`.

No quantitative rate for the divergence of the finite-window Lipschitz constants, no theorem about Hardy `Z` or zeta zeros, and no RH consequence is claimed.

## 1. The enlarged prime orbit is dense in one more torus direction

Consider the joint orbit

`Psi(t)=(Phi_P(t),A_r(t)) in T^(k+1)`.

For an integer character `m=(m_1,...,m_k,m_r)`, the corresponding frequency is

`lambda_m = sum_(j=1)^k m_j log p_j + m_r log r`.

If `lambda_m=0`, exponentiating gives

`prod_(j=1)^k p_j^(m_j) r^(m_r)=1`.

After moving negative exponents to the other side, unique factorization forces every coefficient to vanish. Hence no nonzero integer character has zero frequency.

Exactly as in `VIS-071`, the continuous Weyl criterion then gives

`(1/T) integral_0^T exp(-it lambda_m) dt -> 0`

for every nonzero character. Therefore `Psi(R)` is Haar-equidistributed, and in particular dense, in `T^(k+1)`.

This is the only arithmetic input: the logarithm of the omitted prime is not an integer combination of the retained prime logarithms.

## 2. Density forbids any continuous finite-support decoder

Assume for contradiction that a continuous `F:T^k->C` satisfies

`F(Phi_P(t))=A_r(t)`

for all real `t`.

Its graph

`Gamma_F={(z,F(z)): z in T^k}`

is closed. The joint orbit `Psi(R)` lies in `Gamma_F`, so closure would imply

`T^(k+1)=closure(Psi(R)) subset Gamma_F`.

That is impossible: a graph contains only one output over each `z in T^k`, whereas `T^(k+1)` contains the whole circle of possible final coordinates over the same `z`.

Thus even though exact retained phases identify the height set-theoretically, the omitted prime phase cannot be represented by a continuous function on the retained prime torus.

This gives a stricter boundary than the raw-information statement of `VIS-161`. Set-theoretic height recovery does not make additional prime frequencies continuously available.

## 3. The orbit decoder is nowhere continuous

Because `|P|>=2`, the injectivity argument of `VIS-161` applies to `Phi_P`, so

`f(Phi_P(t))=A_r(t)`

is a well-defined function on the dense orbit `Phi_P(R)`.

Fix any `t_0` and choose any `eta in T` with `eta != A_r(t_0)`. Density of the joint orbit gives a sequence `s_n` such that

`Phi_P(s_n) -> Phi_P(t_0)`,

`A_r(s_n) -> eta`.

Hence `f(Phi_P(s_n))` does not converge to `f(Phi_P(t_0))`. The orbit decoder is discontinuous at `Phi_P(t_0)`. Since `t_0` was arbitrary, it is nowhere continuous.

The instability is therefore not merely a failure to extend continuously at some exceptional recurrence point. Every retained phase state can be approached by heights whose held-out prime phase tends to any prescribed circle value.

## 4. The Lipschitz collision quotient diverges globally

Take `eta=-A_r(t_0)` in the previous argument. Then along a suitable sequence,

`||Phi_P(s_n)-Phi_P(t_0)||_2 -> 0`,

while

`|A_r(s_n)-A_r(t_0)| -> 2`.

Therefore the pairwise quotient from `VIS-162` is unbounded and

`Lambda_P(A_r;R)=infinity`.

By `VIS-162`, this also rules out every exact globally Lipschitz decoder from the retained finite prime torus.

This is a useful matched null for interpreting future collision-complexity experiments: divergence of a zeta observable's `Lambda_P` is not automatically evidence that the observable carries zero-side or non-prime information. The same qualitative divergence occurs for the most elementary source that was simply omitted from `P`.

## 5. Every finite window is regular; the obstruction is global recurrence

For `S=[-T,T]`, the quotient depends only on `Delta=t-u`:

`R_P,r(Delta)=|exp(-i Delta log r)-1| / sqrt(sum_(p in P) |exp(-i Delta log p)-1|^2)`.

When `Delta != 0`, the denominator cannot vanish: simultaneous equality of all retained prime phases would contradict injectivity of `Phi_P`. As `Delta->0`, Taylor expansion gives the finite limit

`R_P,r(Delta) -> (log r)/sqrt(sum_(p in P) (log p)^2)`.

Thus `R_P,r` extends continuously across zero. On the compact interval `|Delta|<=2T`, it is bounded, so

`Lambda_P(A_r;[-T,T])<infinity`.

These constants are nondecreasing in `T`, and their supremum over all `T` is the global quotient already proved infinite. Hence

`Lambda_P(A_r;[-T,T]) -> infinity`.

No useful divergence rate follows from this argument. Such a rate is a simultaneous Diophantine-approximation problem for the retained phases together with a prescribed separated value of the held-out phase.

## 6. Consequence for source-sensitive decoder tests

The accepted prime-phase clue currently asks whether a zeta-facing coordinate escapes a regular decoder class based on a fixed finite prime support. This finding shows that **fixed-support escape is too weak a positive discriminator** for continuous or Lipschitz classes.

A source-sensitive experiment must distinguish at least two mechanisms:

- genuine complexity not explained by prime-phase information at the relevant scale;
- ordinary frequency omission, where the decoder is asked to reconstruct a prime phase whose frequency was never included in its finite support.

For a frozen support `P`, a natural control family is therefore one or more held-out prime phases `r^(-it)` with `r notin P`, preferably chosen under a predeclared frequency/scale matching rule. A zeta-facing collision profile is interesting only if it separates from this omitted-prime baseline under the same metric, height windows, normalization, and decoder budget.

Alternatively, let the retained support `P=P(T)` grow and prove a uniform statement. That route must then account for the changing torus dimension and the corresponding recurrence scale; merely increasing support does not by itself establish source sensitivity.

## 7. Prior art and novelty boundary

The mathematics is classical Kronecker--Weyl theory specialized to prime logarithms. `VIS-071` already records the standard character-average proof and cites Håkan Hedenmalm, Peter Lindqvist, and Kristian Seip, **A Hilbert space of Dirichlet series and systems of dilated functions in L^2(0,1)**, *Duke Mathematical Journal* 86:1 (1997), 1--37, DOI `10.1215/S0012-7094-97-08601-4`, together with the classical Kronecker-theorem literature.

The present graph/density argument is also the standard compact-dynamical fact that an additional irrational torus frequency which is not in the integer character span of the base rotation cannot be a continuous factor coordinate of that base torus flow. No new Kronecker theorem, topological-dynamics factor theorem, or Diophantine approximation rate is claimed.

The Mathia-specific contribution is the control diagnosis created by combining that classical fact with `VIS-161` and `VIS-162`: exact finite prime phases may encode height set-theoretically, yet a held-out prime coordinate already defeats continuous and Lipschitz decoding. Therefore regular-decoder failure against fixed support must be normalized against omitted-source controls before it can be interpreted as zeta-specific structure.

## 8. Boundaries and falsification

The theorem is fixed-finite in the retained prime support and uses exact phases. It does not say that an omitted prime phase is hard to approximate at every finite height or finite numerical resolution. Indeed, each finite window has a finite optimal Lipschitz constant.

It does not compare the **rate** of that finite-window complexity with Hardy `Z`, derivatives, zero occupancy, or other analytic coordinates. Such a comparison is now the live source-sensitive question.

It also does not rule out continuous decoding when the target frequency is already an integer combination of the retained torus frequencies; in that case the corresponding torus character is an explicit continuous decoder. The omitted-prime case is excluded from that character span by unique factorization.

Falsify the no-continuous-decoder claim by constructing continuous `F:T^k->C` with `F(Phi_P(t))=r^(-it)` for all `t`; its graph would then have to contain the dense joint orbit. Falsify the global collision statement by bounding the quotient despite joint orbit points approaching the same retained phase state with opposite held-out phase. Either would contradict the Kronecker--Weyl density established in Section 1.

## Research consequence

The regular-decoder branch remains open, but its next positive test must be **relative**, not merely absolute. Failure of a zeta-facing observable to admit a continuous or Lipschitz decoder from fixed finite support is meaningful only after comparison with held-out prime phases or after a growing-support theorem removes ordinary frequency omission as the explanation.

This narrows the accepted prime-phase recursive-geometry clue without closing it. The next coherent target is a predeclared normalized collision-complexity comparison between a zeta-facing observable and a held-out-prime control under the same finite support, or a theorem showing a separation that persists as the retained prime support grows.