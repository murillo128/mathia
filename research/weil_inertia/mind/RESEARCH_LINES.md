# Weil-inertia research lines

This file records mathematical questions that survive the current Weil-Inertia evidence. It is not a roadmap, task queue, status page, or history.

## Keep source regularity separate from regularity of the canonical defect measure

WI-417--WI-422 identify sharp coercive source-space phenomena for translated-Blaschke probes. With an independently fixed planar density cap, one-target cost has the expected shallow-depth blow-up and critically separated target families converge to a Poisson-capacity problem. Generic TV/Carleson control is too weak because target-adaptive atoms remain cheap. For the bare translated-Blaschke response, ordinary global `L^p` control is bounded exactly for `1<p<2`, with a Lorentz endpoint and different behavior once a finite-TV budget is added.

WI-423 shows why those useful auxiliary spaces cannot simply be imposed on the canonical exact zeta source. The Riesz identity `-Delta U = 2 pi mu_off` makes that source the atomic counting measure of off-critical zeros; exact absolute continuity of the same source would already force the defect measure to vanish. A nontrivial route must therefore generate an auxiliary probe/coefficient source independently and prove an exact or quantitatively controlled coupling from its potential back to the canonical defect measure.

The live question is to derive such an auxiliary source and a target-independent concentration-and-tail budget from accessible prime-side, boundary or explicit-formula data. The norm must be fixed without inspecting hypothetical zero locations and must control the actual Poisson-capacity geometry consumed by the destination.

## Approach the boundary with independently controlled information; transport and canonical Hardy pairing both reproduce the defect

WI-424 identifies the boundary logarithmic derivative of the Kunik Blaschke factor as a canonical positive Poisson defect counter. WI-425--WI-428 show why fixed safe lines and bounded positive or signed multiscale portfolios lose shallow defects unless their cost becomes singular. WI-429 supplies a different bounded category: the positive Hardy projection on `Re(s)=1/2+a` keeps exactly the zeros deeper than `a` and, as `a downarrow0`, retains a fixed fraction of the boundary defect energy. WI-430 extracts the corresponding first-defect quantum, making clear that an unconditional subquantum upper bound would already contain the missing zero-exclusion theorem.

WI-431--WI-434 then audit horizontal continuation from the absolutely convergent prime side. The global positive Hardy projection is zero on `Re(s)>1`; adiabatic localization does not create persistent positive-frequency source leakage; the exact horizontal transport identity splits the interior field into safe-line leakage, a window-edge term and transported residues; and the apparent principal-pole divergence of that edge disappears after exact semigroup transport.

WI-435 gives the decisive matched control. Even if the entire transported edge and safe-line leakage are both `o(1)`, a finite Kunik Blaschke block leaves a nonzero interior Hardy residue field with the full first-defect quantum. Horizontal transport therefore represents the defect more faithfully as its auxiliary errors vanish; it does not upper-bound that defect from independent source information.

WI-436 closes the most canonical mixed-frequency continuation of that idea. For a finite Kunik block and any probe line `0<a<d_*`, the non-Hermitian square of the interior logarithmic derivative satisfies the exact line-invariant identity

`int G_(F,a)(t)^2 dt = ||h_F||_2^2`,

where `h_F` is the positive boundary Poisson flux. Splitting `G_(F,a)=G_++G_-` into Hardy half-spaces gives

`2 int G_+(t)G_-(t) dt = ||h_F||_2^2`.

Thus the simplest translation-invariant bilinear positive/negative-frequency coupling is not killed by Hardy orthogonality; it sees the off-line defect perfectly. But that is exactly the obstruction: the finite-Blaschke matched control saturates it identically, and broad localization converges to the same boundary energy. The bilinear signal is coercive but not **independent**.

The live theorem must therefore introduce information that the finite inner factor cannot reproduce from itself. Adequate categories include a non-translation-invariant or Hankel-type mixed-frequency operator with a symbol justified independently from prime/explicit-formula data, a genuinely nonlinear arithmetic relation between the two Hardy channels, or a boundary/source observable that upper-bounds the interior field without importing reciprocal distances to the same right-half zeros. A canonical bilinear cross pairing, like horizontal transport, may be an exact defect representation and still supply no source constraint.

Every proposal must pass the finite Kunik Blaschke adversarial test: if the proposed source quantity, localization error or mixed-frequency functional can be made small or can be reproduced while the finite block retains its boundary defect energy, it has not supplied independent arithmetic coercivity. A full-zeta passage must additionally handle the lack of a fixed probe depth to the left of all possible off-line zeros; WI-436 is a finite-block theorem and must not be promoted past that domain without a new localization argument.
