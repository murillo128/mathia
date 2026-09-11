# VIS-162 — finite-prime phase collision quotient exactly characterizes Lipschitz decoding

## Claim

Let `P={p_1,...,p_k}` be a finite set of at least two distinct rational primes and define the finite-prime phase map

`Phi_P(t)=(p_1^(-it),...,p_k^(-it)) in T^k subset C^k`.

Equip `T^k` with the chordal Euclidean metric inherited from `C^k`, and write

`D_P(t,u)=||Phi_P(t)-Phi_P(u)||_2`.

By the same unique-factorization argument as `VIS-161`, `Phi_P` is injective. Thus for any `S subset R` and observable `A:S->C`, the **phase-collision quotient**

`Lambda_P(A;S)=sup_(t!=u in S) |A(t)-A(u)|/D_P(t,u)`

is well-defined in `[0,infinity]`.

Then the quotient is exactly the optimal Lipschitz-decoder constant:

`inf { Lip(F) : F:T^k->C, A(t)=F(Phi_P(t)) for every t in S } = Lambda_P(A;S)`,

with the convention that the infimum is infinite when no finite-Lipschitz decoder exists.

Equivalently, for every finite `L>=0`, there exists an exact decoder `F:T^k->C` with `Lip(F)<=L` if and only if

`|A(t)-A(u)| <= L D_P(t,u)`

for every `t,u in S`.

For approximate decoding, if `F:T^k->C` is `L`-Lipschitz and

`sup_(t in S) |A(t)-F(Phi_P(t))| <= epsilon`,

then necessarily

`epsilon >= (1/2) sup_(t,u in S) ( |A(t)-A(u)| - L D_P(t,u) )_+`.

No converse to this approximate bound is claimed.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-KIRSZBRAUN-SPECIALIZATION + REPRESENTATION-OBSTRUCTION + NO-NOVELTY-CLAIM`.

The result does not show that Hardy `Z`, zeta values, zero occupancy, derivatives, or any other specific zeta-facing observable has a large or divergent collision quotient. It converts the Lipschitz branch of the accepted prime-phase clue into an exact pairwise criterion.

## 1. Phase injectivity makes the orbit decoder unambiguous

Suppose `Phi_P(t)=Phi_P(u)`. Choosing any two distinct primes `p,q in P` gives

`(t-u) log p in 2 pi Z`,
`(t-u) log q in 2 pi Z`.

If `t!=u`, division would make `log p/log q` rational, hence some nonzero integer powers of `p` and `q` equal. Unique factorization forbids this. Therefore `t=u`.

Consequently the orbit function

`f:Phi_P(S)->C`,
`f(Phi_P(t))=A(t)`

is well-defined. The question is not whether exact phase data identifies the height — `VIS-161` already shows that it does — but how regular the induced orbit function is in the ambient torus metric.

## 2. Necessity is exactly the collision inequality

If `F:T^k->C` is an exact `L`-Lipschitz decoder, then for every `t,u in S`,

`|A(t)-A(u)|`
` = |F(Phi_P(t))-F(Phi_P(u))|`
` <= L ||Phi_P(t)-Phi_P(u)||_2`
` = L D_P(t,u)`.

Hence `Lambda_P(A;S)<=L`. This already exposes the relevant visual obstruction: two phase states that nearly collide while the observable remains macroscopically separated force a large decoder constant.

Unlike raw information counting, this test is stable-category specific. The exact set-theoretic inverse from `VIS-161` is irrelevant unless it respects the chosen phase metric at a controlled modulus.

## 3. Kirszbraun makes the pairwise bound sufficient

Assume `Lambda_P(A;S)<=L`. The orbit function `f` above is then an `L`-Lipschitz map from the subset `Phi_P(S)` of `C^k ~= R^(2k)` into `C ~= R^2`.

Kirszbraun's extension theorem for Euclidean/Hilbert spaces extends `f` to an `L`-Lipschitz map

`F_bar:R^(2k)->R^2`

with **the same** Lipschitz constant. Restricting `F_bar` to the embedded torus `T^k` gives an exact decoder `F:T^k->C` with `Lip(F)<=L`.

Taking the infimum over `L` proves that the optimal exact decoder constant is precisely `Lambda_P(A;S)`.

This is the load-bearing point: for the chordal finite-prime phase representation, there is no hidden global compatibility condition beyond the pairwise collision inequalities. Searching over neural decoders, Fourier ansatzes, interpolation schemes, or ad hoc formulas cannot improve the optimal Lipschitz constant. The entire exact Lipschitz question is already encoded by the worst phase collision.

## 4. Approximate decoding has an unavoidable collision excess

Let `F` be `L`-Lipschitz and suppose its uniform reconstruction error on `S` is at most `epsilon`. For any `t,u in S`, the triangle inequality gives

`|A(t)-A(u)|`
` <= |A(t)-F(Phi_P(t))|`
`    + |F(Phi_P(t))-F(Phi_P(u))|`
`    + |F(Phi_P(u))-A(u)|`
` <= 2 epsilon + L D_P(t,u)`.

Therefore

`epsilon >= (1/2)(|A(t)-A(u)|-L D_P(t,u))_+`

for every pair, and taking the supremum yields the claimed lower bound.

This bound is useful as a falsification test because one explicit recurrent near-collision can rule out a proposed `(L,epsilon)` decoder budget. It is only a necessary bound: vector-valued Lipschitz approximation can have additional global constraints, and no exact formula for the best approximate error is asserted here.

## 5. Finite-height decoder complexity is a monotone collision profile

For an observable defined on the real axis, set

`Lambda_P(A;T)=Lambda_P(A;[-T,T])`.

Then `Lambda_P(A;T)` is monotone nondecreasing in `T`, and the theorem gives an exact interpretation at every finite height: it is the smallest Lipschitz constant of any torus decoder that reproduces the observable on that window.

Moreover,

`Lambda_P(A;R)=sup_(T>0) Lambda_P(A;T)`.

Hence a global finite-Lipschitz exact decoder exists if and only if the finite-height profile remains uniformly bounded.

For many zeta-facing observables the global exact question is deliberately too coarse. Any globally unbounded observable already cannot be the output of a Lipschitz map on compact `T^k`, because such a map is bounded. The informative object is therefore often the **growth law** of `Lambda_P(A;T)` for a normalized observable or on expanding finite windows, compared with matched phase/clock controls.

The recurrence from `VIS-161` makes that profile nontrivial. There are arbitrarily distant pairs whose phase distance is arbitrarily small. If the corresponding observable differences fail to shrink at the same rate, the required regular decoder complexity must grow.

## 6. Local derivative scale separates ordinary smoothness from recurrent collisions

Let `A` be differentiable at `t`. The phase curve has constant Euclidean speed

`v_P = ( sum_(p in P) (log p)^2 )^(1/2)`.

Indeed,

`D_P(t,t+h)=v_P |h| + o(|h|)`.

Therefore, whenever `A'(t)` exists,

`lim_(h->0) |A(t+h)-A(t)|/D_P(t+h,t) = |A'(t)|/v_P`.

Thus large collision quotients need not come from local roughness. A smooth observable can have a modest local derivative scale yet require a huge global decoder constant because the dense prime-phase orbit brings distant heights close together. That distinction is the visual content of the criterion: **local curve regularity and global recurrence stability are separate gates**.

## 7. Prior art and novelty boundary

The sufficiency direction is a direct specialization of the classical Kirszbraun extension theorem:

- M. Kirszbraun, **Über die zusammenziehende und Lipschitzsche Transformationen**, *Fundamenta Mathematicae* 22:1 (1934), 77–108. Stable EuDML locator: `https://eudml.org/doc/212681`.

McShane's classical real-valued extension theorem is adjacent background, but the complex-valued same-constant extension used here is most naturally covered by the Hilbert-space Kirszbraun theorem:

- E. J. McShane, **Extension of range of functions**, *Bulletin of the American Mathematical Society* 40 (1934), 837–842, DOI `10.1090/S0002-9904-1934-05978-0`.

Mathia's `arithmetic_fidelity` line already contains substantial general Lipschitz-fidelity machinery. In particular, `AF-045` identifies a **lower** Lipschitz modulus with distance to collisions/noninjectivity, while later findings study regular recovery and information-dimension constraints. Those results are not used as evidence for the theorem above and do not duplicate its object: here the question is the **upper** Lipschitz complexity of extending an observable from a dense finite-prime phase orbit to the ambient torus.

No general Lipschitz-extension theorem, phase-retrieval theorem, or zeta theorem is claimed as new. The Mathia-specific step is the representation audit: combining `VIS-161`'s injective-but-ill-conditioned phase encoding with Kirszbraun shows that the accepted clue's Lipschitz-decoder branch has an exact scalar obstruction, the phase-collision quotient.

## 8. Boundaries and falsification

The exact characterization depends on the chosen chordal Euclidean metric on `T^k` and the Hilbert target `C`. A different intrinsic torus metric is bi-Lipschitz equivalent on the compact torus but need not preserve the exact optimal constant, and a non-Hilbert target need not admit a Kirszbraun extension with constant one. These are representation choices, not hidden invariances.

The theorem concerns exact Lipschitz decoders. The approximate collision-excess inequality is only necessary. It also says nothing by itself about computational tractability: a mathematically existing Kirszbraun extension need not be an efficient decoder.

Falsify the exact theorem by exhibiting an `A,S,P` for which all pairwise inequalities hold with constant `L` but no `L`-Lipschitz torus extension exists; that would contradict Kirszbraun in the stated Euclidean embedding. Falsify a claimed zeta application by finding a smaller collision profile or a matched deterministic control with the same profile growth.

Most importantly, do not infer a new zeta information source merely from `Lambda_P(A;T)` growing. The growth may be caused by generic recurrence of the chosen phase representation, amplitude normalization, or a deterministic clock effect. A useful source-sensitive statistic must compare the same frozen observable normalization, prime support, metric, height windows, and control family.

## Research consequence

The Lipschitz option in `CLUE-zeta-prime-phase-recursive-geometry` is now structurally classified. For the finite-prime chordal phase representation, proving or refuting stable Lipschitz recoverability no longer requires searching a decoder class: it is equivalent to controlling one explicit pairwise quantity, `Lambda_P(A;T)`.

The next genuinely zeta-specific question is therefore quantitative. Choose an analytic coordinate and normalization **before** inspecting favorable collisions, freeze `P` and the metric, and determine whether its collision profile grows beyond the matched phase/clock baseline. For Hardy `Z`, zero occupancy, derivatives, or nearby-zero observables, such a result would be new source-side evidence; `VIS-162` itself supplies only the representation criterion, not that evidence.
