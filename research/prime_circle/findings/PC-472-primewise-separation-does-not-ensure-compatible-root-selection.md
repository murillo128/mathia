# PC-472 — Primewise separation does not ensure compatible root selection

**Status:** EXACT-DERIVED + CLASSICAL-STRUCTURE + NEGATIVE/OBSTRUCTION. An infinite rooted admissible support can exclude every unwanted integer by its own prime-residue data and still fail to come from any compatible root phase. The obstruction is simultaneous choice: two holes require different forbidden residues at the same prime. The construction also proves that the exact compatible coding image is not closed under binary intersection, even when the intersection is primewise residue-closed. This is a selection boundary for the existing cotangent limits, not a new spectral law or an RH implication. No historical-priority claim is made.

## 1. Pointwise exclusion and simultaneous exclusion differ

Use the compatible rooted coding of
[[research/prime_circle/findings/PC-471-compatible-root-phases-retain-full-spectrum-but-generically-collapse]], writing forbidden residues `r_p=-a_p` rather than center phases:
\[
\mathcal R_0=\prod_p(\mathbb Z/p\mathbb Z\setminus\{0\}),\qquad
C(r)=\{h\in\mathbb Z:h\not\equiv r_p\pmod p\text{ for every prime }p\},
\qquad \mathcal C_0=\{C(r):r\in\mathcal R_0\}.
\tag{1}
\]
Every such support contains zero and is admissible, meaning that it omits at least one residue modulo each prime. For an arbitrary rooted admissible support `S`, define
\[
\operatorname{cl}_{\rm pr}(S)
=\{h\in\mathbb Z:h\bmod p\in S\bmod p\text{ for every prime }p\}.
\tag{2}
\]
This is the explicitly defined **primewise** closure, not closure in the full profinite topology, which also tests composite moduli. Necessarily
\[
S\in\mathcal C_0\quad\Longrightarrow\quad
\operatorname{cl}_{\rm pr}(S)=S.
\tag{3}
\]
Indeed a hole of `C(r)` is excluded by some selected `r_p`, which is missing from the whole support modulo that prime.

PC-471's factorial example violates (3). The present question is whether imposing (3) repairs its missing compatibility. It does not.

**Theorem.** There is an infinite `S subset Z`, containing zero, such that:

1. `S` is admissible and `cl_pr(S)=S`.
2. `S` is not in `C_0`. More precisely, exactly two compatible rooted supports contain `S`, say `C_1,C_2`, and
   \[
   C_1\cap C_2=S,\qquad 2\in C_1\setminus C_2,\qquad
   4\in C_2\setminus C_1.
   \tag{4}
   \]
3. For the unchanged zero-extended Cauchy operators
   \[
   (L_T)_{hk}=\mathbf1_{h,k\in T}
   \begin{cases}i/[\pi(h-k)],&h\ne k,\\0,&h=k,\end{cases}
   \tag{5}
   \]
   every compatible support `C` containing `S` satisfies
   \[
   \|(L_C-L_S)e_0\|\ge\frac1{4\pi}.
   \tag{6}
   \]
   Nevertheless `L_S` is an arbitrary-moving-center limit under PC-465, and is a strong limit of operators on finite compatible rooted supports.

The theorem compares exact supports and operators. It asserts no difference between their closed spectral sets or spectral types.

## 2. Build the partial sieve while filling every allowed residue

We construct one forbidden nonzero residue `r_q` at each prime `q!=3`, with
\[
T=\{h:h\not\equiv r_q\pmod q\text{ for every prime }q\ne3\},
\qquad S=T\cap3\mathbb Z,
\tag{7}
\]
so that
\[
\{0,2,4\}\subset T,\qquad
S\bmod q=(\mathbb Z/q\mathbb Z)\setminus\{r_q\}\quad(q\ne3).
\tag{8}
\]
In particular the partial sieve preserves both future holes `2,4`; their residue classes must also be represented by retained points divisible by `3` at every other prime.

Enumerate the primes other than `3`. Maintain a finite set `U subset 3Z` containing zero, a finite set `J` of already assigned primes other than `3`, and their frozen residues. Require
\[
V:=U\cup\{2,4\}\text{ to be admissible modulo every prime other than }3,
\qquad v\not\equiv r_p\pmod p\quad(v\in V,\ p\in J).
\tag{9}
\]
Initially `U={0}`, `J` is empty, and `V={0,2,4}` satisfies (9): it occupies only zero modulo `2`, and has three members at primes at least `5`. No admissibility of `V` modulo `3` is required.

At the stage for prime `q!=3`, put `n=|V|+q-1`. Assign every unassigned prime `p!=3` with `p<=n`, and also `q` if needed, a residue missing from `V mod p`. This is possible by (9), and the assigned residue is nonzero because `0 in V`. Keep all previous assignments. Call the resulting finite prime set `J'`.

For each `v mod q` other than `r_q`, choose a new integer `x_v` satisfying
\[
x_v\equiv0\pmod3,\qquad x_v\equiv v\pmod q,\qquad
x_v\equiv0\pmod p\quad(p\in J'\setminus\{q\}).
\tag{10}
\]
The moduli are distinct primes, so CRT supplies infinitely many solutions for each `v`. Choose distinct positive representatives larger than every previous point. All new points avoid every assigned forbidden residue: at `q` this is their definition, and at the other assigned primes they equal zero while `r_p!=0`.

Replace `U` by `U union {x_v:v!=r_q}`. The new `V` has exactly `n` elements. At all assigned primes it still omits the frozen residue; any unassigned prime is larger than `n` and therefore cannot be filled by `V`. This proves (9) for the next stage. At the completed prime `q`, the new `U` represents **every** residue except `r_q`.

Repeat indefinitely. Every prime other than `3` is eventually assigned and processed. Old assignments never change, every installed point remains retained, and infinitely many distinct points are installed. Let `U_infinity` be their union with zero. Then
\[
U_\infty\subset T\cap3\mathbb Z=S,
\]
and the completed stages give the inclusion of every allowed residue in (8). The reverse inclusion follows from the definition of `T`. The protected points `0,2,4` belong to `T` because every assignment avoided the current `V`.

Additional survivors of the partial sieve are allowed. The proof does **not** identify `S` with `U_infinity` or discard those survivors: (7) defines the actual support, and the residue equalities follow from the installed witnesses and the permanent exclusions together.

## 3. The exact obstruction has only one prime coordinate

Since zero is retained,
\[
S\bmod3=\{0\};
\]
together with (8), this proves admissibility. It also gives the exact closure identity
\[
\operatorname{cl}_{\rm pr}(S)
=\{h:h\equiv0\pmod3,\ h\not\equiv r_q\pmod q\ (q\ne3)\}
=S.
\tag{11}
\]
For every prime `q!=3`, both `2 mod q` and `4 mod q` occur in `S mod q`, because `2,4` were protected in `T` and (8) fills all its allowed residues. Thus the only prime which could remove either hole without removing some member of `S` is `3`. But `2 mod3=2` and `4 mod3=1`. One forbidden residue at `3` cannot remove both.

More precisely, any compatible phase preserving `S` must use the uniquely missing `r_q` at every `q!=3`. At prime `3` it has only the two choices `1,2`. Consequently the only compatible supersets are
\[
C_1=T\setminus(1+3\mathbb Z),\qquad
C_2=T\setminus(2+3\mathbb Z).
\tag{12}
\]
They contain zero, are both of the form (1), and satisfy (4). This proves that even the intersection of two exact compatible supports need not be compatible, despite satisfying the complete primewise closure test.

One can express the failure in terms of the available exclusion primes
\[
W_h(S)=\{p:h\bmod p\notin S\bmod p\}.
\tag{13}
\]
Primewise closure requires `W_h(S)` to be nonempty for each hole. In this construction `W_2(S)=W_4(S)={3}`, with incompatible required values at that coordinate. The issue is the consistency of simultaneous choices, not a failure to find an individual witness.

For comparison, if every hole of a rooted admissible `S` has **infinitely many** available primes in (13), then `S` is compatible. In the nonempty compact product
\[
\prod_p((\mathbb Z/p\mathbb Z)\setminus(S\bmod p)),
\]
the phases killing a fixed hole form an open dense set: a finite cylinder leaves a fresh available prime at which to kill it. Baire's theorem, applied to the countably many holes, gives a phase killing all of them while preserving `S`. This sufficient condition explains the fresh-prime argument for finite supports; it is not asserted to be necessary or to classify all infinite supports.

## 4. Consequence for cotangent selection, and its limit

[[research/prime_circle/findings/PC-465-moving-center-cotangent-limits-fill-the-admissible-hull]] proves boundedness of (5) on every admissible support and realizes it by moving finite-sieve centers. Since `S` is admissible, that theorem applies. Since zero belongs to every rooted support, the nonzero entries of column zero in (5) identify exactly its nonzero retained offsets. Thus `L_S` cannot equal `L_C` for any compatible rooted support `C`, whether or not containment is assumed beforehand.

For a compatible completion `C` containing `S`, (12) forces retention of either `2` or `4`, both absent from `S`. The corresponding entry of `(L_C-L_S)e_0` has magnitude `1/(2pi)` or `1/(4pi)`, respectively, proving (6).

This separation is specifically from **completions preserving all of `S`**. It is not separation from the closure of the compatible family. The finite sets
\[
F_R=S\cap[-R,R]
\]
are rooted and admissible, hence are exact compatible supports by PC-471's fresh-prime exclusion construction. Their masks converge pointwise to `S`. The Cauchy column-tail bound and uniform operator bound in PC-465 imply `L_(F_R) -> L_S` strongly. Their realizing phases may change at previously used primes; that is precisely what one globally compatible phase cannot do here.

There is no new conclusion about the limiting spectral set, spectral type, zeta zeros or RH. The mathematical delta is a strict improvement over the pointwise obstruction in PC-471: even complete primewise separation fails, because the geometry of root selection requires one jointly consistent forbidden-residue assignment.

## 5. Prior art, controls and validation

The coding is classical. S. Kasjan, G. Keller and M. Lemańczyk, *Dynamics of B-free sets: a view through the window*, **IMRN 2019**, 2690–2734, DOI [10.1093/imrn/rnx196](https://doi.org/10.1093/imrn/rnx196), [manuscript](https://arxiv.org/pdf/1702.02375), §1.1, supplies the group/window coding used in (1). The sign change from their phase coordinates to forbidden residues changes no object.

G. Keller, *Generalized heredity in B-free systems*, **Stochastics and Dynamics 21** (2021), article 2140008, DOI [10.1142/S0219493721400086](https://doi.org/10.1142/S0219493721400086), [manuscript](https://arxiv.org/pdf/1704.04079), §1.1, Theorem 1 and Corollary 1, distinguishes the coding image from its closure `X_phi` and proves heredity of that closure in the proximal case. The overline in the definition of `X_phi` is essential. Nonclosure of the exact image under intersection does not contradict that theorem. The primewise-closed counterexample and its two compatible completions are constructed directly above; they are not attributed to the general heredity theorem.

Local searches covered residue closure, simultaneous exclusion, compatible phases and coding intersections. External checks covered B-free window images, admissibility and generalized heredity. The result uses elementary CRT, cardinality and Baire arguments within established coding theory. These checks do not establish historical novelty; the retained result is the explicit obstruction and its exact operator-selection consequence.

The obstruction is already classical finite-choice geometry once the infinite residue witnesses are installed. Neither divergence of the prime-reciprocal sum nor a zeta identity enters the proof. The CRT extension uses distinct coprime moduli and cardinality bounds; the contradiction uses one coordinate with two incompatible required values. It supplies no prime-specific spectral selector.

An exact-integer Python audit under `/tmp` ran **54** saturation-extension stages under three deterministic missing-residue policies, processing all **18** primes other than `3` through `67`. Each run installed **548** retained witnesses and froze **100** prime coordinates; the largest coordinates had **224** digits. All **513** completed-residue checks passed, as did **6,003** finite-window checks of (12)'s intersection identity. Every stage checked preservation of old phases, all retained and protected points, admissibility away from `3`, the filled residue classes and the two incompatible hole exclusions. These are finite diagnostics of the construction, not a substitute for its infinite proof.

The proof is not Lean-verified or independently adversarially approved. Its load-bearing infinite step is preservation of every installed residue witness under all later exclusions; the argument explicitly keeps all additional survivors. A finite-prefix obstruction by itself would not suffice, since a later untested prime could otherwise remove a hole. No compute or formalization executor is enrolled: the elementary finite-choice contradiction alone does not capture this infinite realization boundary.
