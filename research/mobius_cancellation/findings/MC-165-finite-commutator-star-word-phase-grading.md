# MC-165 — Finite prime-commutator *-words collapse to a two-sector Möbius phase grading on square-free inputs

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `BOUNDARY/CONDITIONAL-GAIN`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the canonical number-state representation

\[
\mathcal H=\ell^2(\mathbb N),
\qquad
S_p\varepsilon_n=\varepsilon_{pn},
\]

and the square-free multiplicative phase family from `MC-163`–`MC-164`,

\[
f_z(n)=
\begin{cases}
\displaystyle\prod_{p\mid n}z_p,&n\text{ squarefree},\\
0,&n\text{ otherwise},
\end{cases}
\qquad |z_p|=1,
\]

with diagonal `D_z\varepsilon_n=f_z(n)\varepsilon_n` and

\[
C_p^{(z)}=[D_z,S_p].
\tag{1}
\]

The Möbius specialization is `z_p=-1` for every prime, so `D_z=D_\mu`.

Let

\[
W=X_r\cdots X_1
\tag{2}
\]

be any finite word in the raw prime commutators and their adjoints. Write

\[
X_j=
\begin{cases}
C_{p_j}^{(z)},&\sigma_j=+1,\\
(C_{p_j}^{(z)})^*,&\sigma_j=-1,
\end{cases}
\]

allowing repeated primes, and define the signed word charge

\[
q(W):=\sum_{j=1}^r\sigma_j.
\tag{3}
\]

Fix the divisibility pattern of the square-free input `n` at the finitely many primes occurring in `W`. On each such local support cell there is a deterministic exponent path. If the path is illegal, `W\varepsilon_n=0`. If it is nonzero, then there are:

- a final basis state `n_W`, obtained from `n` by the prime-exponent path of the word; and
- a scalar `K_{W,\eta}(z)` depending only on the word, the initial local support pattern `\eta`, and the phases of primes occurring in the word,

such that

\[
\boxed{
W\varepsilon_n
=
f_z(n)^{q(W)}K_{W,\eta}(z)\,\varepsilon_{n_W}.
}
\tag{4}
\]

Moreover `K_{W,\eta}(z)` is a finite product of one-prime finite-difference factors and Laurent monomials in the local `z_p`; the global input phase from primes outside the word occurs only through the single charge factor `f_z(n)^{q(W)}`. Thus mixed adjoints do not manufacture an additional nonfactorizing state-phase invariant.

For Möbius, `f_z(n)=\mu(n)` on the square-free sector and `\mu(n)^{-1}=\mu(n)`. Since

\[
q(W)\equiv r\pmod 2,
\tag{5}
\]

equation `(4)` collapses to an exact two-sector law. There exists a phase-free finite partial weighted shift `T_W`, determined only by the word and finitely many prime-divisibility conditions, such that

\[
\boxed{
W P_{\rm sf}
=T_W D_\mu^{\,r}P_{\rm sf}.
}
\tag{6}
\]

Equivalently,

\[
\boxed{
W P_{\rm sf}
=\begin{cases}
T_WP_{\rm sf},&r\text{ even},\\
T_WD_\mu P_{\rm sf},&r\text{ odd}.
\end{cases}
}
\tag{7}
\]

The theorem includes repeated-prime words and arbitrary mixtures of adjoints, so it closes the two explicit monomial boundaries left by `MC-163` and `MC-164` on the square-free input sector relevant to Möbius summation.

A finite noncommutative *-polynomial therefore has the normal form

\[
\boxed{
A(C,C^*)P_{\rm sf}
=T_0P_{\rm sf}+T_1D_\mu P_{\rm sf},
}
\tag{8}
\]

where `T_0` and `T_1` are finite sums of phase-free local partial weighted shifts. Finite raw *-polynomial algebra supplies only two Möbius phase sectors on square-free inputs: a support/divisibility sector and a sector carrying the original Möbius orientation linearly. It does not generate a third relational phase class between them.

This is an information classification, not a Mertens estimate. An odd-sector coefficient can be masked, sparse, averaged away, or otherwise difficult to use; equation `(8)` does not claim that every polynomial with `T_1\ne0` is globally Mertens-complete. It says that any Möbius phase retained by a finite raw *-polynomial enters linearly through the same `D_\mu` orientation rather than through a newly generated cross-prime phase.

## 1. One commutator or adjoint contributes exactly one phase charge

Write

\[
b_p^{(z)}(m):=f_z(pm)-f_z(m).
\tag{9}
\]

Then

\[
C_p^{(z)}\varepsilon_m=b_p^{(z)}(m)\varepsilon_{pm},
\tag{10}
\]

and

\[
(C_p^{(z)})^*\varepsilon_m
=\begin{cases}
\overline{b_p^{(z)}(m/p)}\,\varepsilon_{m/p},&p\mid m,\\
0,&p\nmid m.
\end{cases}
\tag{11}
\]

For square-free `s`,

\[
b_p^{(z)}(s)=
\begin{cases}
(z_p-1)f_z(s),&p\nmid s,\\
-f_z(s),&p\mid s.
\end{cases}
\tag{12}
\]

Thus every nonzero occurrence of `C_p^{(z)}` contributes one factor `f_z(s)` evaluated at a square-free state, while every nonzero occurrence of its adjoint contributes one conjugate factor `\overline{f_z(s)}`.

The only possible temporary nonsquarefree state in a nonzero path is created when `C_p^{(z)}` acts on a square-free state already containing `p`, producing a `p^2` factor. If the word continues, the next nonzero letter must be `(C_p^{(z)})^*`; any other raw commutator or adjoint evaluates a finite difference on a nonsquarefree predecessor and vanishes. Hence every coefficient factor in a nonzero path is still evaluated on a square-free state, even when the path makes such a one-step squareful excursion.

## 2. Every square-free evaluation state differs from the input only by local prime toggles

Let `P(W)` be the finite set of primes occurring in the word. Start from a square-free `n` and follow a nonzero path. Every square-free state `s` at which a coefficient in `(12)` or its conjugate is evaluated differs from `n` only in the membership of primes in `P(W)`.

Therefore

\[
f_z(s)=f_z(n)\,\chi_s(z),
\tag{13}
\]

where `\chi_s(z)` is a Laurent monomial in the finitely many `z_p`, `p\in P(W)`, determined by the local support path. In particular, `\chi_s` is independent of all prime phases outside the word.

If `X_j=C_{p_j}^{(z)}`, equation `(13)` contributes one factor `f_z(n)` times a local phase monomial. If `X_j=(C_{p_j}^{(z)})^*`, it contributes `\overline{f_z(n)}=f_z(n)^{-1}` times a conjugate local monomial. Multiplying all `r` factors gives exactly

\[
f_z(n)^{N_+-N_-}=f_z(n)^{q(W)},
\tag{14}
\]

where `N_+` and `N_-` are the numbers of commutator and adjoint letters. All remaining finite-difference factors and local phase monomials form `K_{W,\eta}(z)`. This proves `(4)`.

No commutativity of the operators is assumed. Order is retained in the local exponent path and in `K_{W,\eta}`; the statement is only that the dependence on the **global input phase** has a one-dimensional charge law.

## 3. Möbius reduces charge to degree parity

At `z_p=-1`, every square-free phase is real of order two:

\[
f_z(n)=\mu(n)\in\{\pm1\}.
\]

Hence

\[
\mu(n)^{q(W)}=\mu(n)^r,
\tag{15}
\]

because `q(W)-r=-2N_-` is even. On each local support cell the remaining coefficient `K_{W,\eta}(-1)` depends only on the word path and takes an explicit real value built from the local amplitudes `1` and `2` and their signs.

Grouping those support cells produces a finite partial weighted shift `T_W` that is independent of the value of `\mu(n)` itself, and `(6)`–`(7)` follow.

This extends both previous special cases:

- `MC-163` corresponds to charge-zero quadratic words `(C_p)^*C_q`; their input phase cancels before any scalarization.
- `MC-164` corresponds to adjoint-free words, for which `q(W)=r`; even degree loses the phase and odd degree carries it.

The extension is not merely notational because repeated primes and adjoint backtracking allow squareful intermediate states that neither earlier theorem classified in general.

## 4. Repeated-prime examples obey the same grading

The simplest repeated-prime identities make the boundary concrete. On square-free inputs,

\[
\boxed{
C_p^2P_{\rm sf}
=-2S_{p^2}P_{\rm sf}(I-P_p),
}
\tag{16}
\]

so the even word has no Möbius sign coefficient. A third forward step dies,

\[
\boxed{
C_p^3P_{\rm sf}=0,
}
\tag{17}
\]

because the second step has already created a `p^2` state.

The two quadratic backtracking words are also support-only:

\[
\boxed{
C_p^*C_pP_{\rm sf}=P_{\rm sf}(4I-3P_p),
}
\tag{18}
\]

and

\[
\boxed{
C_pC_p^*P_{\rm sf}=4P_{\rm sf}P_p.
}
\tag{19}
\]

By contrast a single adjoint is odd and carries the input sign on its domain:

\[
\boxed{
C_p^*P_{\rm sf}=2S_p^*D_\mu P_{\rm sf}P_p.
}
\tag{20}
\]

These examples also stress-test the temporary-squareful case: a forward step into exponent `2` can be followed only by the matching adjoint if the path is to remain nonzero, and the resulting even pair removes the Möbius phase exactly.

## 5. Finite *-polynomials have a two-sector normal form

Let `A(C,C^*)` be any finite linear combination of finite words. Split its monomials by degree parity. Applying `(7)` termwise gives

\[
A(C,C^*)P_{\rm sf}
=\sum_{r\text{ even}}T_WP_{\rm sf}
+\sum_{r\text{ odd}}T_WD_\mu P_{\rm sf}.
\]

Absorb the finite sums into `T_0` and `T_1` to obtain `(8)`.

Thus mixing even and odd words can create interference between a phase-free baseline and a masked linear copy of the Möbius orientation, but it cannot create a new nonlinear phase generated by the raw finite *-algebra itself. Any claimed cancellation gain from such a polynomial must therefore come from a separate quantitative theorem about the phase-free transport/masking operators, a state or averaging functional, or another structure not contained in the bare word algebra.

This sharpens the residual boundary after `MC-164`: passing from adjoint-free words plus isolated Gram terms to **all finite words in the commutators and their adjoints** does not create an intermediate phase category on the square-free sector.

## 6. Prior-art and novelty audit

The Bost–Connes system and its canonical semigroup representation are classical; see J.-B. Bost and A. Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica 1 (1995), 411–457, DOI `10.1007/BF01589495`. Semigroup crossed-product/dilation structure around the Bost–Connes system is standard, including M. Laca, *From Endomorphisms to Automorphisms and Back: Dilations and Full Corners*, Journal of the London Mathematical Society 61 (2000), 893–904, DOI `10.1112/S0024610799008492`. Twisted commutator/spectral-triple constructions for Bost–Connes-type quantum statistical systems are also established prior art; see M. Greenfield, M. Marcolli and K. Teh, *Type III sigma-spectral triples and quantum statistical mechanical systems*, arXiv `1305.5492`.

Words in weighted shifts, adjoints, local support projections, and degree/gauge bookkeeping are standard operator-algebraic mechanisms. A targeted search for Bost–Connes prime-isometry commutator *-words, Möbius diagonals, mixed commutator/adjoint words, phase charge, and parity grading did not locate this exact square-free Möbius specialization. Search absence is not evidence of novelty, and the proof above is elementary once the represented action is fixed. The finding therefore makes **no novelty claim**.

The durable delta is internal and exact: `MC-163` explicitly left mixed adjoint/non-adjoint words outside its Gram theorem, while `MC-164` explicitly left all mixed words and repeated-prime words outside its adjoint-free classification. Equations `(4)`–`(8)` close those finite raw-word boundaries simultaneously on square-free inputs.

## Boundaries and falsification tests

- **Square-free input sector.** The operator identities `(6)`–`(8)` are restricted on the right by `P_sf`. This is the sector that contributes nonzero Möbius coefficients to `M(x)`, but it is not a classification of the full operator action on arbitrary nonsquarefree starting states. For example an adjoint can act nontrivially on a state with one exponent equal to `2` by reading the neighboring square-free predecessor.
- **Finite words and finite polynomials.** Norm closures, infinite series, resolvents, unbounded operators, or limiting functional calculi are not covered. A claimed gain from such a completion requires convergence and information-retention analysis rather than automatic extension of `(8)`.
- **Raw commutator generators only.** Coefficient-algebra insertions, Hamiltonian weights, KMS states, twisted commutators, modular conjugations, or other source-defined operations can change the path amplitudes or the phase bookkeeping and are outside the theorem unless reduced explicitly to the present generators.
- **Two-sector form is not a global decoder theorem.** `T_1\ne0` does not imply that one fixed scalar readout reconstructs every `\mu(n)`. A sparse or averaging `T_1` may still lose orientation information. The theorem classifies the phase dependence that survives, not the quantitative stability of recovering `M(x)`.
- **Phase-free does not mean arithmetically trivial.** `T_0` and `T_1` can retain square-free support, divisibility, exponent-path and ordering information. The claim is only that no additional Möbius orientation phase is generated by the finite raw word algebra.
- **Matched phase family is diagnostic.** Arbitrary `z_p` controls need not satisfy Möbius-specific arithmetic theorems. They are used only to isolate the state-phase charge carried by the represented operator word.
- **No RH input.** The proof uses the local square-free multiplicative phase law and exact basis action only. No zero-free region, contour shift, explicit formula, Mertens bound, or RH-equivalent estimate enters.
- **Direct falsification.** A counterexample is a finite mixed word, a square-free input, and a nonzero path for which the coefficient cannot be factored as `(4)`, or at Möbius phase a word violating `(7)`. The one-step formulas `(10)`–`(13)` exhaust every nonzero letter in such a path.

## Consequence for the line

The finite raw commutator *-algebra is now classified at the phase level relevant to square-free Möbius inputs. Increasing word length, introducing adjoints, backtracking, or repeated primes does not by itself escape the earlier support-versus-target dichotomy: every finite polynomial reduces to a phase-free transport sector plus a sector that carries `D_\mu` linearly.

A surviving Bost–Connes/noncommutative route therefore needs a mathematically new ingredient rather than a more elaborate finite word in the same generators. Plausible remaining categories include source-forced coefficient-algebra insertions that create a nonseparable prime interaction, a twisted or modular operation that changes the charge law, or an infinite/analytic completion with a rigorously controlled limit and an independent arithmetic estimate. Any such route must still show quantitative advantage after the line's target-reencoding and Mertens-transfer tests; richer operator notation alone is not an escape.