# AF-258 — Periodic completeness is governed by a congruence-uniform cancellation exponent

**Status:** `EXACT-DERIVED`, `DIOPHANTINE-FIDELITY`, `OUTPUT-SAMPLING`, `PROFINITE-COVERAGE`, `LI-DOMINANT-MODE-CONTROL`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-257 classifies the worst two-mode Li cancellation over **all unbounded** retained index sets by the ambient half-integer exponent. That is stronger than the sampling class used in AF-247--AF-248, where the retained set is required to visit every residue class modulo every integer infinitely often. For that periodically complete class, the exact obstruction is not the ambient exponent but a congruence-uniform envelope.

Let `alpha` be irrational and define

\[
d_\alpha(n)=\operatorname{dist}\!\left(n\alpha,\mathbb Z+\frac12\right),
\qquad
A_\alpha(n)=\frac{-\log d_\alpha(n)}{n}.
\tag{1}
\]

For an unbounded set `S subset N`, let

\[
\tau_\alpha(S)
=\liminf_{\substack{n\to\infty\\n\in S}}A_\alpha(n).
\tag{2}
\]

Call `S` **periodically complete** when

\[
\forall q\ge1,\ \forall r\in\mathbb Z/q\mathbb Z,
\qquad
|S\cap(r+q\mathbb Z)|=\infty.
\tag{3}
\]

For each congruence cylinder define

\[
K_{q,r}(\alpha)
:=
\limsup_{\substack{n\to\infty\\ n\equiv r\ (\mathrm{mod}\ q)}}
A_\alpha(n),
\tag{4}
\]

and define the **profinite cancellation exponent**

\[
\boxed{
K_{\mathrm{pc}}(\alpha)
:=
\inf_{q\ge1}\ \min_{r\in\mathbb Z/q\mathbb Z}
K_{q,r}(\alpha).
}
\tag{5}
\]

Then

\[
\boxed{
\sup_{S\ \mathrm{periodically\ complete}}
\tau_\alpha(S)
=
K_{\mathrm{pc}}(\alpha).
}
\tag{6}
\]

Consequently, for the conjugate two-mode signal

\[
F_{\alpha,m}(n)=-2m\cos(\pi n\alpha),
\qquad m\ge1,
\tag{7}
\]

AF-249 gives the exact constrained worst case

\[
\boxed{
\inf_{S\ \mathrm{periodically\ complete}}
\limsup_{\substack{n\to\infty\\n\in S}}
|F_{\alpha,m}(n)|^{1/n}
=
\exp\!\bigl(-K_{\mathrm{pc}}(\alpha)\bigr).
}
\tag{8}
\]

For one hypothetical off-critical Keiper pair with radial factor `q_\rho>1`, the pair-level version is

\[
\boxed{
\inf_{S\ \mathrm{periodically\ complete}}
\limsup_{\substack{n\to\infty\\n\in S}}
|q_\rho^nF_{\alpha_\rho,m}(n)|^{1/n}
=
q_\rho\,e^{-K_{\mathrm{pc}}(\alpha_\rho)}.
}
\tag{9}
\]

In particular:

- every periodically complete retained set preserves the **full pair rate** `q_\rho` if and only if `K_pc(alpha_rho)=0`;
- there is a uniform strictly superunit margin over all periodically complete sets if and only if
  \[
  K_{\mathrm{pc}}(\alpha_\rho)<\log q_\rho;
  \tag{10}
  \]
- if `K_pc(alpha_rho)>log q_rho`, then some periodically complete set suppresses the pair below unit root rate;
- at the boundary `K_pc(alpha_rho)=log q_rho`, the infimum in `(9)` is exactly one, while attainment by one retained set is a separate question.

The ambient AF-257 exponent is recovered from the trivial modulus:

\[
K_{\mathrm{pc}}(\alpha)
\le
K_{1,0}(\alpha)
=
\kappa_{1/2}(\alpha)
=
2L_{\mathrm{oe}}(\alpha).
\tag{11}
\]

The inequality can be maximally strict. There exists an irrational `alpha` with

\[
\boxed{
\kappa_{1/2}(\alpha)=+\infty
\qquad\text{but}\qquad
K_{\mathrm{pc}}(\alpha)=0.
}
\tag{12}
\]

Thus even a super-Liouville half-integer cancellation profile can be completely harmless for **every periodically complete** retained set when all exponentially dangerous approximants are trapped away from one congruence cylinder. Ambient irrationality base, or even the exact AF-257 ambient exponent, does not by itself classify fidelity once the sampler is required to retain profinite coverage.

## Why it matters

AF-248 proves that periodic completeness can fail catastrophically for a specially constructed transcendental Li-shaped mode. AF-249 and AF-257 then sharpen the unconstrained obstruction until it is exactly the parity-filtered continued-fraction growth `2L_oe(alpha)`. A natural reading would be that the same source theorem is needed even when the actual compression is known to retain every finite congruence class.

Equation `(6)` shows that this is false. Periodic completeness changes the quantifier structure. A bad retained set must now obtain its exponential cancellation while visiting **every** profinite cylinder infinitely often. A cancellation spike confined to one arithmetic region can be avoided only by an arbitrary sparse sampler; a periodically complete sampler is forced to keep returning to any cylinder on which the phase has subexponential cancellation.

The simplest useful corollary is therefore

\[
\boxed{
\exists(q,r)\;K_{q,r}(\alpha)=0
\quad\Longrightarrow\quad
K_{\mathrm{pc}}(\alpha)=0.
}
\tag{13}
\]

One safe congruence cylinder is enough to force full two-mode root-rate fidelity for **all** periodically complete retained sets. This is substantially weaker than AF-257's all-unbounded-set condition `kappa_{1/2}(alpha)=0`.

The explicit construction proving `(12)` also separates two superficially similar super-Liouville regimes. AF-248 constructs a phase whose catastrophic indices can themselves be arranged periodically complete. The phase below has equally severe ambient exponential approximation, but every dangerous principal-convergent event lies at an even sample index; the odd cylinder is asymptotically safe. The difference is therefore not the strength of approximation but its **profinite distribution**.

## Exact derivation

### 1. Any periodically complete sampler is bounded by every congruence cylinder

Let `S` satisfy `(3)`. For every fixed pair `(q,r)`, the subset

\[
S_{q,r}:=S\cap(r+q\mathbb Z)
\]

is infinite. Hence

\[
\tau_\alpha(S)
=
\liminf_{\substack{n\to\infty\\n\in S}}A_\alpha(n)
\le
\liminf_{\substack{n\to\infty\\n\in S_{q,r}}}A_\alpha(n)
\le
K_{q,r}(\alpha).
\tag{14}
\]

Since `(14)` holds for every congruence cylinder,

\[
\tau_\alpha(S)\le K_{\mathrm{pc}}(\alpha).
\tag{15}
\]

Taking the supremum over periodically complete `S` gives the upper bound in `(6)`.

### 2. Diagonal selection attains every exponent below the congruence envelope

Fix

\[
0\le c<K_{\mathrm{pc}}(\alpha).
\tag{16}
\]

By `(5)`, for every `(q,r)` one has `K_{q,r}(alpha)>c`. Therefore the set

\[
E_{q,r}(c)
:=
\{n\ge1:n\equiv r\pmod q,\ A_\alpha(n)>c\}
\tag{17}
\]

is infinite.

Choose a sequence of congruence requirements

\[
(q_1,r_1),(q_2,r_2),\ldots
\tag{18}
\]

in which every pair `(q,r)` occurs infinitely many times. Inductively choose

\[
n_j\in E_{q_j,r_j}(c),
\qquad n_j>n_{j-1}.
\tag{19}
\]

This is always possible because each set in `(17)` is infinite. Put `S_c={n_j:j\ge1}`. Every congruence pair occurs infinitely often in `(18)`, so `S_c` is periodically complete, while `(19)` gives

\[
\tau_\alpha(S_c)\ge c.
\tag{20}
\]

Letting `c` increase to `K_pc(alpha)` proves the reverse inequality in `(6)`. If `K_pc(alpha)=+infinity`, the same construction works for every finite `c`, so the supremum is `+infinity` in the extended sense.

AF-249 gives

\[
\limsup_{\substack{n\to\infty\\n\in S}}
|F_{\alpha,m}(n)|^{1/n}
=e^{-\tau_\alpha(S)}.
\tag{21}
\]

Since the exponential is decreasing and continuous on the extended half-line, `(6)` immediately yields `(8)`, and multiplication by the fixed radial factor `q_rho^n` yields `(9)`.

Because every `A_alpha(n)` is nonnegative, `K_pc(alpha)=0` implies `tau_alpha(S)=0` for every periodically complete `S`, proving the full-rate statement. The strict and non-strict threshold claims follow directly from `(9)` and the distinction between an infimum and its possible attainment.

### 3. A super-Liouville phase whose bad events are confined to even sample indices

We now construct the strict separation `(12)` using the AF-257 continued-fraction classification.

Write

\[
\alpha=[0;a_1,a_2,a_3,\ldots]
\tag{22}
\]

and let `P_j/Q_j` be its principal convergents, with

\[
Q_{-1}=0,
\qquad
Q_0=1,
\qquad
Q_j=a_jQ_{j-1}+Q_{j-2}.
\tag{23}
\]

Set

\[
a_1=4.
\tag{24}
\]

After `Q_{2j-1}` has been defined, choose

\[
a_{2j}
=
\left\lceil e^{Q_{2j-1}^2}\right\rceil,
\qquad
 a_{2j+1}=4
\quad(j\ge1).
\tag{25}
\]

The recurrence `(23)` gives inductively

\[
\boxed{
Q_{2j-1}\equiv0\pmod4,
\qquad
Q_{2j}\equiv1\pmod4.
}
\tag{26}
\]

Indeed, `Q_1=4` and `Q_2=a_2Q_1+Q_0 congruent 1 (mod 4)`. If `(26)` holds at one stage, then

\[
Q_{2j+1}=4Q_{2j}+Q_{2j-1}\equiv0\pmod4,
\]

and the next huge partial quotient multiplies a multiple of four, so

\[
Q_{2j+2}=a_{2j+2}Q_{2j+1}+Q_{2j}\equiv1\pmod4.
\]

Thus **every even convergent denominator is in fact divisible by four**. Moreover `(25)` gives

\[
\frac{\log Q_{2j}}{Q_{2j-1}}
\ge
\frac{\log a_{2j}}{Q_{2j-1}}
\ge Q_{2j-1},
\tag{27}
\]

up to an irrelevant vanishing rounding error. Hence AF-257 implies

\[
\kappa_{1/2}(\alpha)
=
2\limsup_{\substack{j\to\infty\\Q_j\ \mathrm{even}}}
\frac{\log Q_{j+1}}{Q_j}
=+\infty.
\tag{28}
\]

So this `alpha` is maximally bad for unrestricted sparse sampling.

### 4. The odd congruence cylinder has zero exponential cancellation

We claim

\[
K_{2,1}(\alpha)=0.
\tag{29}
\]

Suppose instead that `(29)` fails. Then some `c>0` and infinitely many **odd** `n` satisfy

\[
A_\alpha(n)\ge c.
\tag{30}
\]

For each such `n`, choose the nearest odd integer `p_n` as in AF-257, so

\[
\left|\alpha-\frac{p_n}{2n}\right|
=
\frac{d_\alpha(n)}{n}.
\tag{31}
\]

Reduce `p_n/(2n)` by

\[
g_n=\gcd(p_n,2n).
\tag{32}
\]

Because `p_n` is odd, `g_n` is odd. Since `n` is also odd, the reduced denominator is

\[
s_n=\frac{2n}{g_n}
\equiv2\pmod4.
\tag{33}
\]

But `(30)` makes `(31)` exponentially smaller than `1/(2s_n^2)` for all sufficiently large `n`. Legendre's criterion therefore forces the reduced rational to be a principal convergent of `alpha`, exactly as in AF-257. Its denominator would then be a convergent denominator congruent to `2 mod 4`, contradicting `(26)`.

Therefore `(29)` holds. Equation `(5)` now gives

\[
0\le K_{\mathrm{pc}}(\alpha)
\le K_{2,1}(\alpha)=0,
\]

which proves `K_pc(alpha)=0` and completes `(12)`.

Combining `(28)` with `(8)` gives the sharp contrast:

\[
\inf_{S\ \mathrm{unbounded}}
\limsup_{n\in S}|F_{\alpha,m}(n)|^{1/n}=0,
\qquad
\inf_{S\ \mathrm{periodically\ complete}}
\limsup_{n\in S}|F_{\alpha,m}(n)|^{1/n}=1.
\tag{34}
\]

The same phase is therefore maximally unfaithful under unrestricted sparse sampling and perfectly root-faithful under periodic completeness.

## Prior-art audit

The underlying ingredients are classical. The topology generated by congruence classes and the profinite completion of the integers are standard; `(3)` is simply recurrent coverage of every finite congruence cylinder. The diagonal selection in `(17)`--`(20)` is elementary and no novelty is claimed for it as an abstract selection lemma.

Shrinking-target and recurrence problems with arithmetic/dynamical constraints are an established subject. Rosenblatt and Roychowdhury, **“Geometric and Measure-Theoretic Shrinking Targets in Dynamical Systems,”** arXiv:`1809.09780`, is one nearby general reference already used in AF-254. Dong Han Kim, Seul Bee Lee, and Lingmin Liao, **“Diophantine approximation by rational numbers of certain parity types,”** *Mathematika* 71 (2025), e12285, DOI `10.1112/mtk.12285`, is direct prior art for parity-restricted rational approximation and continued-fraction algorithms, as audited in AF-257.

A targeted search for shrinking-target approximation constrained to recurrent coverage of every residue class, and for continued-fraction denominator conditions modulo four, did not locate the exact minimax identity `(6)` or the specific separation `(34)`. This is not an exhaustive novelty proof. The durable Arithmetic Fidelity contribution is narrow: once the compression contract itself requires periodic completeness, the correct exponential-fidelity invariant is the worst congruence-cylinder limsup `(5)`, not the ambient AF-257 exponent, and these two invariants can differ from `+infinity` to zero on one irrational phase.

## Boundaries and failure modes

**This is still a two-mode theorem.** The scalar target is the half-integer zero set of one cosine. Several co-dominant Keiper phases require a congruence-uniform version of the AF-253 quotient-fiber norm rather than `(5)` verbatim.

**Periodic completeness is a strong compression contract.** The result does not say an arbitrary source-access or coefficient-sampling scheme is periodically complete. It says that once this coverage property is independently guaranteed, AF-257's all-unbounded-set source condition is unnecessarily strong.

**`K_pc` is exact but not yet known for a Riemann zero.** The theorem changes the source question; it does not prove that the actual normalized Keiper phase has one safe congruence cylinder.

**The continued-fraction construction is a control, not a zeta model.** It proves strict logical separation between ambient and periodically complete fidelity. It does not assert that zero-derived phases have the modular pattern `(26)`.

**The full Li sequence still needs remainder separation.** Equation `(9)` is pair-level. As in AF-255, transfer to the whole Li coefficient sequence requires the retained pair rate to remain above the root rate of the remainder on the same sampling class.

## Research consequence

The source-specific frontier after AF-257 should now be matched to the actual compression contract. If the intended retained index family is only required to be unbounded, the exact obstruction remains `2L_oe(alpha_rho)`. If it is periodically complete, the correct obstruction is instead `K_pc(alpha_rho)`.

This opens a strictly weaker source route. To prove full two-mode fidelity for every periodically complete sampler, it is enough to identify **one** modulus and residue class on which the normalized Keiper phase cannot approach half-integers exponentially. A zeta-specific theorem need not control all parity-selected continued-fraction jumps. Conversely, AF-248 shows that no conclusion follows from periodic completeness alone: a sufficiently congruence-rich super-Liouville phase can still make `K_pc=+infinity`.

The next useful arithmetic audit is therefore not merely whether `alpha_rho` has irrationality base one. It is whether any known or derivable property of the actual zero-derived phase excludes exponential half-integer approximation on at least one fixed congruence cylinder. That is a smaller and more structured source theorem than the all-unbounded-set condition isolated in AF-257.