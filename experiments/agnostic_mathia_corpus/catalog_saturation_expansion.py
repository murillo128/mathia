from __future__ import annotations


from experiments.agnostic_mathia_corpus.catalog_depth import deep_unit


SATURATION_UNIT_SPECS = [
    deep_unit(
        "qf_set_quotient_coequalizer",
        "quotients_and_factorization",
        "hott_book_578b85c",
        "A set quotient freely turns a relation into equality",
        "Chapter 6, Section 6.10, definition of A/R and Lemma 6.10.3 (quotient universal property)",
        "For a type A with a relation R, the higher-inductive set quotient A/R has a point q(a) for every a in A, a path q(a)=q(b) for every witness of R(a,b), and a constructor forcing the result to be a set. A map from A/R into a set B is therefore determined by a map f:A→B that identifies every R-related pair. The recursion principle constructs the descended map, while induction and set-truncation make it unique. The theorem expresses this as the same universal property as the coequalizer of the two projections from the type of related pairs to A. The imposed paths generate the effective equivalence; no separate choice of representatives is needed, and the set constructor prevents unintended higher path data from surviving.",
        """The construction tells us exactly what “close a relation under equality” costs. The point and path constructors add the requested identifications; set-truncation then fixes the level at which the quotient is meant to live. Without that last constructor, the same generators can retain higher coherence rather than form an ordinary set.

The universal property is the operational test. To define an observer on the quotient, define it before quotienting and prove that it cannot distinguish related inputs. Uniqueness then says there is no hidden representative-dependent choice. This resembles a group quotient, but the source relation need not begin as a congruence or equivalence: the higher-inductive construction freely supplies the equality structure, while the intended codomain controls how much coherence must be checked.""",
        representations=["higher_inductive_type", "coequalizer", "universal_property"],
        concepts=["set_quotient", "descent", "truncation"],
        moves=["abstraction", "synthesis", "analogy_boundary"],
        epistemic_role="construction_and_universal_property",
        geometry_role="meaningful_bridge",
        depth_contribution="distinct quotient construction with generated paths, truncation, and a mapping theorem",
    ),
    deep_unit(
        "sa_polya_cycle_index",
        "symmetry_and_actions",
        "applied_combinatorics_2017_3",
        "The cycle index refines fixed-point averaging into a reusable inventory",
        "Chapter 15, Section 15.4.1, cycle index and Theorem 15.11 (Pólya Enumeration Theorem)",
        "Let a finite permutation group G act on a finite set of positions. For each permutation g, record c_i(g), the number of cycles of length i, and average the monomial x_1^{c_1(g)}x_2^{c_2(g)}⋯ over G. This cycle-index polynomial retains more information than the number of orbits. When colors have weights, a coloring fixed by g must be constant on every cycle of g; a cycle of length i colored with a color of weight w contributes w^i. Substituting the sum of i-th powers of the color weights for x_i therefore gives the inventory of coloring orbits by total weight. The proof is Burnside’s lemma applied coefficientwise: the substituted monomial enumerates fixed colorings of one permutation, and the group average converts fixed-coloring counts into orbit counts.",
        """Burnside asks, “how many orbits?” Pólya asks a richer question: “how many orbits of each composition?” The cycle index is the interface that lets one answer many weighted coloring questions without recounting the group action from scratch.

The key compression is by cycle type. A fixed coloring cannot vary inside a permutation cycle, so the apparently global fixed-point constraint factors into independent cycle choices. Substitution then restores the application-specific palette. This is not a generic license to substitute into any orbit average: it depends on colors combining multiplicatively across disjoint cycles and on a finite action. Change the local decoration rule or introduce interactions between cycles, and the inventory requires a different state space.""",
        representations=["permutation_cycles", "cycle_index", "weighted_generating_function"],
        concepts=["group_action", "fixed_point", "orbit_inventory"],
        moves=["compression", "change_of_representation", "synthesis"],
        epistemic_role="worked_enumeration_transform",
        geometry_role="meaningful_bridge",
        depth_contribution="weighted orbit enumeration beyond univariate Burnside counting",
    ),
    deep_unit(
        "dc_jordan_chains",
        "decomposition_and_canonical_forms",
        "axler_linear_algebra_done_right_4e_2026",
        "Jordan chains expose the nilpotent motion inside one generalized eigenspace",
        "Chapter 8, Section 8C, Examples 8.42–8.43 and Theorems 8.45–8.46 (Jordan form)",
        "For an operator T on a finite-dimensional complex vector space, split the space into generalized eigenspaces. On the generalized eigenspace for λ, the shifted operator N=T−λI is nilpotent. The nilpotent structure is represented by chains v,Nv,… ending at zero; when the vectors are ordered along these chains, N has ones immediately above the diagonal and zeros elsewhere. Adding λI produces Jordan blocks. The nilpotent-basis theorem supplies a basis made of such chains, and concatenating the bases from all generalized eigenspaces yields a Jordan basis for T. The sizes of the blocks measure how long generalized eigenvectors take to enter the kernel. Thus eigenvalues alone do not classify the operator: two operators can have the same spectrum and multiplicities but different chain-length data and hence fail to be similar.",
        """A defective operator is not “almost diagonal” in a vague sense. Jordan form names the residue precisely: after the eigenvalue is removed, a nilpotent shift moves each basis vector one step down a finite chain.

This gives a useful diagnostic hierarchy. First locate generalized eigenspaces; then inspect the growth of kernels of powers of T−λI; finally infer the block lengths that produce those dimensions. Diagonalizability is the boundary case in which every chain has length one. The basis is not canonical and small perturbations can change Jordan structure dramatically, so the form is a classification of exact similarity, not a numerically stable coordinate system.""",
        representations=["generalized_eigenspace", "nilpotent_chain", "Jordan_block"],
        concepts=["similarity", "nilpotence", "canonical_form"],
        moves=["decomposition", "invariant_tracking", "prediction_falsification"],
        epistemic_role="classification_proof_anatomy",
        geometry_role="absent",
        depth_contribution="worked generalized-eigenvector mechanism distinguishing spectrum from full similarity type",
    ),
    deep_unit(
        "du_fenchel_conjugate",
        "duality_objects_and_constraints",
        "boyd_vandenberghe_convex_2009",
        "Fenchel conjugacy replaces a function by all of its affine lower tests",
        "Chapter 3, Section 3.3, conjugate function, examples, Fenchel inequality, and biconjugate discussion",
        "For an extended-real function f on a vector space, its conjugate is f*(y)=sup_x(yᵀx−f(x)). Because it is a supremum of affine functions of y, f* is convex even when f is not. The defining inequality f(x)+f*(y)≥yᵀx is Fenchel’s inequality. If f is closed and convex, conjugating again recovers f: f**=f; without those hypotheses exact recovery can fail because affine supporting tests need not retain nonconvex detail. For a positive-definite quadratic f(x)=xᵀQx/2, optimizing the affine-minus-quadratic expression gives f*(y)=yᵀQ⁻¹y/2, so curvature is inverted. For an indicator of a set, the conjugate is its support function, turning membership constraints into directional extrema. These examples show that the same transform exchanges curvature, constraints, and supporting directions through one supremum construction.",
        """Conjugacy converts values at primal points into answers to a family of slope tests. A dual vector asks how large the linear reward yᵀx can be after paying f(x); the conjugate records the best answer.

Three boundaries matter:

- convexity of f* follows from the construction, not from convexity of f;
- exact recovery by f** needs closed convex structure;
- differentiability or a unique optimizer needs stronger hypotheses still.

The transformation can therefore both reveal and erase. It reveals supporting slopes and turns several operations into dual operations, but a nonconvex function can lose precisely the dents that affine tests cannot see. That loss is why biconjugacy is a closure theorem rather than a universal involution.""",
        representations=["extended_real_function", "supporting_affine_tests", "dual_function"],
        concepts=["Fenchel_conjugate", "biconjugate", "convex_envelope"],
        moves=["duality", "reframing", "analogy_boundary"],
        epistemic_role="transform_with_exactness_boundary",
        geometry_role="primary",
        depth_contribution="function-level duality with explicit loss and recovery conditions",
    ),
    deep_unit(
        "ic_rational_canonical",
        "invariants_and_classification",
        "broida_williamson_canonical_forms_cc0",
        "Invariant factors classify an operator without splitting its polynomial",
        "Chapter 8, Section 8.5, Theorems 8.11–8.16 on cyclic decomposition and rational canonical form",
        "View a finite-dimensional vector space with operator T as a module over the polynomial ring by letting x act as T. The structure theorem decomposes this module into cyclic summands whose annihilating polynomials, the invariant factors, divide one another. Choosing a cyclic generator in each summand gives the basis v,Tv,…, and the matrix of T on that basis is the companion matrix of the corresponding invariant factor. Placing these companion matrices on the diagonal gives rational canonical form. The ordered invariant factors are uniquely determined, so two matrices over the same field are similar exactly when their rational canonical forms agree. Unlike Jordan form, this construction does not require the characteristic polynomial to split into linear factors; irreducible polynomials can remain intact, making the classification valid over an arbitrary field.",
        """Rational canonical form changes the classification question from “which eigenvectors exist?” to “how does the polynomial ring act?” That move avoids leaving the base field.

The companion blocks are concrete coordinates, but their real content is the divisibility chain of invariant factors. One can test a proposed classification by checking whether it records enough module structure to reconstruct those factors; trace, determinant, and characteristic polynomial alone generally do not. Over a splitting field the same information can be reorganized into primary and Jordan data, yet the two forms answer different representation needs. Rational form is field-respecting and exact, not necessarily the most geometrically transparent or numerically robust.""",
        representations=["polynomial_module", "companion_matrix", "invariant_factors"],
        concepts=["similarity", "rational_canonical_form", "classification"],
        moves=["abstraction", "decomposition", "change_of_representation"],
        epistemic_role="complete_classification",
        geometry_role="absent",
        depth_contribution="field-independent operator classification beyond incomplete scalar invariants",
    ),
    deep_unit(
        "spd_immersion_open_rank",
        "stability_perturbation_deformation",
        "walpuski_differential_geometry_2021",
        "Compactness turns pointwise full rank into stable immersion",
        "Section 8.5, Theorem 8.60 and proof (stability of rank, immersions, submersions, and local diffeomorphisms)",
        "Matrices of rank at least r form an open subset of the space of linear maps because the nonvanishing of one r-by-r minor persists under small perturbations. For a smooth map f, the derivative df varies continuously with the base point and with f in the C¹ topology. If f is an immersion on a compact domain, every df_x has maximal rank. Each point therefore has a neighborhood and a C¹ tolerance on which maximal rank persists. Compactness extracts finitely many such neighborhoods, and the minimum of their tolerances gives one global perturbation size. Every map sufficiently C¹-close to f remains an immersion. The same argument treats submersions and local diffeomorphisms with their corresponding rank conditions. Compactness is what upgrades local open conditions to one uniform neighborhood of the map.",
        """The proof has two scales. Linear algebra says full rank is locally stable at one derivative. Compactness says finitely many local margins can protect every derivative at once.

This distinguishes stability from homotopy invariance. An immersion survives sufficiently small C¹ perturbations because derivatives remain in an open rank stratum; a large continuous deformation may cross the rank-deficient boundary. C⁰ closeness is also insufficient, since it controls values but not derivatives. Whenever a qualitative property is presented as stable, ask which jet or norm sees the property, whether the good locus is open there, and what supplies a uniform margin over the domain.""",
        representations=["derivative_bundle", "rank_stratum", "C1_topology"],
        concepts=["immersion", "openness", "compactness"],
        moves=["linearization", "local_global", "prediction_falsification"],
        epistemic_role="stability_proof",
        geometry_role="primary",
        depth_contribution="worked local-to-uniform stability mechanism with topology and compactness hypotheses",
    ),
    deep_unit(
        "dit_parametric_transversality",
        "dimension_intersection_transversality",
        "walpuski_differential_geometry_2021",
        "A transverse total family makes almost every slice transverse",
        "Section 8.2, Theorem 8.21 and proof (parametric transversality)",
        "Let F:P×M→N be a smooth family of maps f_p:M→N, and suppose F is transverse to a submanifold Z of N. Then W=F⁻¹(Z) is a submanifold. Consider the projection π:W→P. At a point (p,x), the slice f_p is transverse to Z exactly when p is a regular value of π at that point: surjectivity of dπ encodes whether variations in x, together with tangent directions of Z, cover the missing directions in N. Sard’s theorem says the critical values of π have measure zero. Hence for almost every parameter p, f_p is transverse to Z. The conclusion is genericity in the parameter family, not transversality of every slice, and it depends on transversality of the combined evaluation map F.",
        """A perturbation theorem is hiding a second map. Instead of checking all slices independently, assemble them into one total map and study the bad parameters as critical values of a projection.

Proof flow: pull the target submanifold back through the total family; project that incidence manifold to parameter space; translate slice failure into projection criticality; apply Sard. This architecture explains both the power and the caveat. “Almost every” is measure-theoretic and need not identify a preferred parameter, while a poorly chosen family whose total map is not transverse offers no genericity guarantee. The parameter directions must actually be capable of repairing the missing normal directions.""",
        representations=["parameter_family", "incidence_submanifold", "critical_values"],
        concepts=["transversality", "genericity", "Sard_theorem"],
        moves=["auxiliary_object", "reframing", "finite_infinite_transfer"],
        epistemic_role="genericity_proof_anatomy",
        geometry_role="primary",
        depth_contribution="family-scale transversality proof distinct from one-map preimage dimension counting",
    ),
    deep_unit(
        "pc_projective_atlas",
        "projectivization_and_compactification",
        "walpuski_differential_geometry_2021",
        "Projective charts normalize scale without choosing it globally",
        "Section 1, Example 1.39, equations (1.40)–(1.46), projective space atlas and transition maps",
        "Real projective n-space is the quotient of nonzero vectors in R^{n+1} by nonzero scalar multiplication. For each coordinate i, let U_i consist of lines whose i-th coordinate is nonzero. Every line in U_i has a unique representative whose i-th coordinate equals one, so deleting that coordinate defines a chart to R^n. On an overlap U_i∩U_j, changing from the i-normalized representative to the j-normalized one divides all coordinates by the nonzero j-th coordinate and permutes the omitted slot. These rational transition maps are smooth wherever the denominator is nonzero, so the charts define a smooth atlas. No single normalization covers all lines: the quotient has no globally preferred nonzero coordinate, and the overlaps record how the local choices of scale agree.",
        """Projectivization removes scale globally, while a chart temporarily puts scale back by declaring one coordinate to be one. The transition map is the audit trail for that temporary choice.

This makes the manifold structure source-specific rather than pictorial. Coverage follows because every nonzero vector has some nonzero coordinate; uniqueness of normalized representatives makes each chart well defined; nonzero overlap denominators make the transitions smooth. An affine chart is therefore not the whole projective space plus a decorative boundary. Different charts are equally legitimate local gauges, and the omitted hyperplane becomes visible precisely where one chosen normalization fails.""",
        representations=["quotient", "affine_chart", "transition_map"],
        concepts=["projective_space", "atlas", "gauge_choice"],
        moves=["geometricization", "local_global", "change_of_representation"],
        epistemic_role="worked_manifold_construction",
        geometry_role="primary",
        depth_contribution="chart-level projective construction beyond the scale-equivalence definition",
    ),
    deep_unit(
        "mp_elliptic_j_moduli",
        "moduli_and_parameter_spaces",
        "mit_elliptic_curves_18_783_f25",
        "The j-invariant classifies geometric elliptic curves but not all arithmetic forms",
        "Lecture 13, Section 13.2, Definition 13.11 and Theorems 13.12–13.14 on the j-invariant and twists",
        "For a Weierstrass model of an elliptic curve, the quantities c₄ and the discriminant transform with matching weights under admissible coordinate changes, so j=c₄³/Δ is unchanged by isomorphism. Every value of j over a field occurs for some elliptic curve, subject to the characteristic-sensitive formulas in the notes. Over an algebraic closure, two elliptic curves have the same j-invariant exactly when they are isomorphic. Over the original field, equality of j can fail to imply isomorphism: distinct twists become isomorphic only after extending scalars. Thus the affine j-line is a coarse parameter space for geometric isomorphism classes, while arithmetic forms over a fixed field retain descent data that one scalar cannot encode.",
        """Here a coarse moduli coordinate succeeds and fails in one example. It succeeds after passage to an algebraic closure: j records the geometric isomorphism class. It fails to classify all objects over the ground field because twisting data disappears after that passage.

The right question is therefore not simply “is j complete?” but “complete for which equivalence and over which base?” Automorphisms and descent separate a point of the coarse line from a family-level moduli object. This provides a concrete boundary for moduli slogans: a parameter may name every geometric class and still omit the identifications needed to pull families back canonically.""",
        representations=["Weierstrass_model", "invariant_coordinate", "coarse_moduli_line"],
        concepts=["j_invariant", "twist", "descent"],
        moves=["classification", "analogy_boundary", "prediction_falsification"],
        epistemic_role="worked_coarse_moduli_example",
        geometry_role="primary",
        depth_contribution="explicit invariant with algebraic-closure classification and ground-field failure boundary",
    ),
    deep_unit(
        "ho_van_kampen_codes",
        "homotopy_and_obstruction",
        "hott_book_578b85c",
        "Van Kampen computes paths in a pushout by normalizing alternating local paths",
        "Chapter 8, Section 8.7, construction of code and the encode–decode proof of the van Kampen theorem",
        "For a pushout P of a span A←C→B, paths between points inherited from A and B can be represented by finite alternating sequences of local paths, with crossings supplied by points of C. These raw sequences carry redundancies: identity segments, composition of adjacent local pieces, and the pushout gluing paths must be related. The chapter defines a set-level code by quotienting the sequences by the generated relations. An encode map sends an actual path in P to its code by path induction and transport. A decode map composes the represented local paths and gluing paths in P. The two maps are shown inverse, yielding an equivalence between the fundamental-groupoid path set and the combinatorial code. The result requires set truncation because the theorem computes the fundamental groupoid, not all higher paths of the pushout.",
        """Van Kampen is a local-to-global theorem with an explicit intermediate language. The code remembers enough order to compose local paths across the gluing interface, while quotient relations discard syntactic choices that do not change the resulting global path.

Encode–decode divides the burden cleanly: encoding proves every global path has a symbolic account; decoding proves every well-formed account denotes a path; the inverse laws prove the relations are neither too weak nor too strong. This is deeper than saying that fundamental groups “glue.” The truncation level, base objects, and coherence relations determine which global homotopy information is actually reconstructed; higher homotopy needs a richer interface.""",
        representations=["pushout", "alternating_path_code", "fundamental_groupoid"],
        concepts=["van_Kampen", "encode_decode", "gluing"],
        moves=["synthesis", "compression", "bridge_construction"],
        epistemic_role="encode_decode_proof",
        geometry_role="primary",
        depth_contribution="worked path-gluing computation beyond a single-space loop calculation",
    ),
    deep_unit(
        "up_pullback_fiber_product",
        "universal_properties_and_canonicality",
        "riehl_category_context_2016",
        "A pullback is a product constrained by agreement over a base",
        "Chapter 3, Definition 3.1.15 and Example 3.2.9 (pullbacks and fiber products of sets)",
        "Given maps f:X→Z and g:Y→Z, a pullback is an object P with projections to X and Y whose composites to Z agree. It is universal among such compatible pairs: for every object W with maps a:W→X and b:W→Y satisfying f∘a=g∘b, there is a unique map W→P inducing both. In sets, P is the fiber product {(x,y)∈X×Y | f(x)=g(y)} with coordinate projections. Existence is thus a constrained product construction, while uniqueness up to unique isomorphism follows from the mapping property. When Z is terminal, the compatibility equation is automatic and the pullback reduces to an ordinary product. When X and Y are subsets over a common ambient set, a pullback can represent their intersection, but that concrete picture does not define pullbacks in every category.",
        """The ordinary product pairs arbitrary choices. The pullback pairs only choices that tell the same story after mapping to a shared base.

That compatibility equation is the extra semantic content. It predicts where the construction appears: synchronized state, base change, intersections, and spaces of solutions to matching constraints. The universal property also separates construction from canonicality; a subset of a Cartesian product is one model in sets, while another category may build the same interface differently. Calling every pullback an intersection is therefore too narrow, and calling it merely a product forgets the commuting square that selects its admissible pairs.""",
        representations=["commutative_square", "fiber_product", "mapping_property"],
        concepts=["pullback", "compatibility", "universal_property"],
        moves=["abstraction", "synthesis", "analogy_boundary"],
        epistemic_role="definition_and_concrete_realization",
        geometry_role="meaningful_bridge",
        depth_contribution="compatibility-constrained universal construction distinct from an unconstrained product",
    ),
    deep_unit(
        "fit_henkin_term_model",
        "finite_infinite_transfer",
        "open_logic_2026_snapshot",
        "Henkin witnesses turn syntactic consistency into a model",
        "First-Order Logic, Completeness: Henkin Expansions, Construction of a Model, and Completeness Theorem",
        "Start with a consistent first-order theory. Extend the language by adding a fresh constant to witness each existential formula, together with an axiom saying that if the existential holds then the chosen instance holds. The Henkin expansion is arranged conservatively so consistency is preserved. Extend the resulting theory to a complete consistent Henkin theory. Its term model takes closed terms as provisional elements and identifies two terms when their equality belongs to the theory; function symbols act by forming terms, and relation symbols hold exactly when the corresponding atomic sentence is in the theory. The truth lemma proves by induction on formulas that satisfaction in this model agrees with membership in the complete theory. Consequently every consistent theory has a model, and semantic consequence implies formal derivability by contraposition.",
        """Completeness does not summon a model from consistency in one jump. It engineers a language in which existential commitments have names, then lets syntax serve as the carrier of a structure.

Each stage repairs a specific obstruction. Henkin constants prevent unnamed witnesses; completion decides every sentence needed by the truth lemma; quotienting terms by provable equality makes interpretation well defined. The final induction is the bridge that licenses the syntactic construction semantically. This is a finite-to-infinite passage through an explicit growing theory, not the same mechanism as ultraproduct compactness or topological compactness, even though all can turn local consistency into existence.""",
        representations=["Henkin_language", "term_model", "truth_lemma"],
        concepts=["completeness", "witness", "syntactic_model"],
        moves=["auxiliary_object", "synthesis", "finite_infinite_transfer"],
        epistemic_role="model_construction_proof",
        geometry_role="absent",
        depth_contribution="full syntax-to-semantics construction with witness, quotient, and induction stages",
    ),
    deep_unit(
        "aor_integral_flow_relaxation",
        "auxiliary_objects_and_relaxations",
        "applied_combinatorics_2017_3",
        "Network structure makes a linear relaxation recover an integral flow",
        "Chapter 13, Section 13.6 and Theorem 14.1, integer-capacity maximum flow and the linear-programming formulation",
        "A maximum-flow problem can be written as a linear program: edge variables obey capacity inequalities and flow-conservation equalities, while the objective maximizes net flow from source to sink. Dropping an explicit integrality requirement appears to enlarge the feasible set to fractional flows. For integer capacities, however, the augmenting-path algorithm begins with the zero integral flow and augments by the minimum residual capacity on a path. Residual capacities remain integers, so every update remains integral; termination produces an integral maximum flow. Thus the linear optimum is attained by an integral feasible point in this structured problem. The conclusion is not true for arbitrary linear programs with integer coefficients. It arises from the network incidence constraints and the residual augmentation mechanism, which also produces a cut certificate of optimality.",
        """This is a successful relaxation, but the reason is not “linear programs round nicely.” The network gives a revision operation that preserves integrality step by step and a dual obstruction that certifies when revision is finished.

The example suggests a disciplined relaxation audit:

1. identify what discrete constraint was dropped;
2. locate a structural theorem or algorithm that restores an integral optimum;
3. distinguish existence of one integral optimum from integrality of every feasible point;
4. test whether the same argument survives outside the network matrix.

Without that structure, a fractional optimum can be genuinely better. Integrality is a theorem about this feasible geometry, not a default consequence of integer input data.""",
        representations=["linear_program", "residual_network", "integral_polytope"],
        concepts=["relaxation", "integrality", "maximum_flow"],
        moves=["reframing", "auxiliary_object", "prediction_falsification"],
        epistemic_role="worked_zero_gap_relaxation",
        geometry_role="meaningful_bridge",
        depth_contribution="positive integrality mechanism complementing the existing relaxation-gap warning",
    ),
    deep_unit(
        "cbp_baire_one_boundary",
        "counterexamples_and_boundary_phenomena",
        "lebl_basic_analysis_v52",
        "Dense discontinuity is compatible with a pointwise limit, but everywhere discontinuity is not",
        "Chapter 6, Section 6.2, Exercises 6.2.16–6.2.17 on the popcorn and Dirichlet functions",
        "The popcorn function on an interval assigns zero at irrational points and, at a rational written in lowest terms, a height that decreases with its denominator. It is discontinuous at every rational and continuous at every irrational, so its discontinuity set is dense; nevertheless the exercise constructs it as a pointwise limit of continuous functions. The Dirichlet function, equal to one on rationals and zero on irrationals, is discontinuous at every point and is not a pointwise limit of continuous functions. It can still be obtained as a pointwise limit of functions that are themselves pointwise limits of continuous functions. The contrast locates a genuine hierarchy: dense discontinuities do not by themselves obstruct Baire class one, but everywhere oscillation does, while one more limiting layer can recover the function.",
        """A moving spike teaches that pointwise convergence can lose continuity. These two functions ask how badly it can fail.

The answer is not measured just by density. The popcorn function has bad points in every interval, yet its discontinuities are interleaved with continuity points and it remains a first pointwise limit. Dirichlet oscillation leaves no continuity point anywhere, crossing the Baire-one boundary while entering at the next level. A useful counterexample strategy is therefore to track the descriptive complexity of the failure set and the number of limiting operations, not merely to maximize how many exceptional points appear.""",
        representations=["oscillatory_function", "pointwise_limit_hierarchy", "discontinuity_set"],
        concepts=["Baire_class", "pointwise_convergence", "boundary_example"],
        moves=["counterexample_construction", "classification", "prediction_falsification"],
        epistemic_role="paired_boundary_counterexamples",
        geometry_role="meaningful_bridge",
        depth_contribution="hierarchy-scale boundary distinguishing dense from everywhere discontinuity",
    ),
    deep_unit(
        "ag_projective_group_law",
        "arithmetic_geometry",
        "mit_elliptic_curves_18_783_f25",
        "Collinearity turns a cubic curve into a group",
        "Lecture 2, Sections 2.1–2.3, projective Weierstrass curves and the geometric group law",
        "A smooth projective Weierstrass cubic has a distinguished point O at infinity. For points P and Q, draw the line through them, using the tangent when P=Q. Bezout-style intersection counting gives a third intersection R with the cubic, counted with multiplicity. Reflect R across the horizontal axis to define P+Q. Equivalently, three collinear intersection points sum to O. The point O acts as identity, reflection gives inverses, and rational formulas in the coordinates show that the sum of points defined over a field remains defined over that field whenever the denominators are valid; projective treatment covers the exceptional vertical and infinite cases. Associativity is the non-obvious axiom: it follows from the algebraic geometry of divisors or from a separate geometric argument, not from the drawing alone.",
        """The group law is a translation between incidence and algebra. A line-cutting construction produces an operation whose closure is visible in projective geometry and whose arithmetic is expressed by rational functions.

The diagram predicts the identity and inverse immediately, but it does not certify associativity. That asymmetry matters: some axioms are local consequences of the construction, while the deepest one uses global structure of the cubic. Singular cubics also change the story. Smoothness and the distinguished projective point are not presentation details; together they make the geometric recipe a genuine elliptic-curve group rather than an appealing partial operation.""",
        representations=["projective_cubic", "secant_tangent", "rational_group_law"],
        concepts=["elliptic_curve", "group_law", "collinearity"],
        moves=["geometricization", "bridge_construction", "prediction_falsification"],
        epistemic_role="geometric_algebraic_construction",
        geometry_role="primary",
        depth_contribution="worked arithmetic operation whose group structure is created by projective incidence",
    ),
    deep_unit(
        "ag_isogeny_kernel_quotient",
        "arithmetic_geometry",
        "mit_elliptic_curves_18_783_f25",
        "Finite kernels determine separable isogeny quotients",
        "Lecture 5, Theorems 5.8 and 5.11, kernels, separable degree, and quotients by finite subgroups",
        "An isogeny is a nonconstant morphism of elliptic curves that sends identity to identity and hence is a group homomorphism. For a separable isogeny, the order of its kernel equals its degree. Conversely, given a finite subgroup G of an elliptic curve over a suitable field, the notes construct a separable isogeny φ:E→E/G whose kernel is exactly G; the target and map are unique up to isomorphism. Translation by elements of G leaves the quotient map unchanged, so functions on the target correspond to G-invariant functions on E. The degree records how many generic points are identified, while inseparability is the boundary where scheme-theoretic degree can exceed the number of geometric kernel points. Thus the kernel controls a quotient map, but only with the separability and field-of-definition qualifications stated in the theorem.",
        """This resembles the first isomorphism theorem, but geometry adds two audits. Is the map separable, so geometric points count the degree correctly? Is the subgroup defined over the base in the sense needed for the quotient to descend?

Once those questions are settled, the kernel is controlled forgetting: points in one G-orbit receive the same image, invariant functions descend, and the target is canonical up to the appropriate isomorphism. The analogy with an abstract group quotient helps predict the factorization, while the morphism, smooth-curve, and field conditions mark exactly where the analogy stops.""",
        representations=["finite_subgroup", "isogeny", "quotient_curve"],
        concepts=["kernel", "separability", "degree"],
        moves=["structural_transfer", "quotienting", "analogy_boundary"],
        epistemic_role="structure_theorem_with_boundary",
        geometry_role="primary",
        depth_contribution="kernel-quotient mechanism enriched by degree, separability, and descent",
    ),
    deep_unit(
        "ag_frobenius_hasse_bound",
        "arithmetic_geometry",
        "mit_elliptic_curves_18_783_f25",
        "Frobenius converts finite-field point counting into an endomorphism bound",
        "Lecture 7, Theorem 7.3 and proof of Hasse’s theorem",
        "For an elliptic curve E over a finite field F_q, the q-power Frobenius endomorphism π fixes exactly the F_q-rational points, so E(F_q)=ker(π−1). The map π−1 is separable, and the kernel-size/degree theorem therefore expresses the point count as deg(π−1)=q+1−t, where t is the trace of Frobenius. For integers r and nonzero s, expanding the degree of rπ−s gives the nonnegative quantity q r²−t rs+s². After division by s², density of the rationals shows that qx²−tx+1 is nonnegative for every real x. Its discriminant t²−4q must therefore be nonpositive. Hence |t|≤2√q and the point count lies in the Hasse interval. Enumeration has been replaced by algebra of one geometric endomorphism and positivity of degree.",
        """The finite set of rational points is recognized as a fixed-point set. That reframing makes counting accessible to invariant algebra: kernel size becomes degree, and degree positivity bounds the trace.

This is a conceptual compression with arithmetic consequences. The curve may have many equations and points, yet the count is controlled by the trace term in a quadratic degree expression. The spectral analogy is useful—trace and discriminant resemble a two-dimensional characteristic polynomial—but should not be overstated: the proof lives in an endomorphism ring with a geometric degree form, not in an arbitrary matrix norm. Smooth elliptic structure is doing the work.""",
        representations=["Frobenius_endomorphism", "fixed_points", "quadratic_relation"],
        concepts=["point_count", "trace", "Hasse_bound"],
        moves=["reframing", "invariant_tracking", "compression"],
        epistemic_role="quantitative_bound_proof_anatomy",
        geometry_role="primary",
        depth_contribution="advanced arithmetic-geometric fixed-point argument with an exact quantitative consequence",
    ),
    deep_unit(
        "sp_stationary_return_time",
        "stochastic_processes",
        "mit_stochastic_processes_18_445_s15",
        "Stationary mass is the reciprocal scale of return time",
        "Course archive member static_resources/2edaa8542469ce692226813a8bd1ec88_MIT18_445S15_lecture2.pdf, Lecture 2, irreducible finite Markov chains, stationary distribution and mean return-time formula",
        "For an irreducible Markov chain on a finite state space, there is a unique stationary distribution π satisfying πP=π. If τ_x^+ is the first positive return time to state x, then π(x)=1/E_x[τ_x^+]. One proof decomposes a long trajectory into excursions from x to x. Each excursion begins and ends at x, and the expected number of visits to any state during a typical excursion gives an invariant measure; normalizing by the expected excursion length produces π. The x-coordinate contributes one visit per excursion, giving the reciprocal return-time formula. Irreducibility makes all states communicate and the normalization finite. Aperiodicity is not needed for existence or the formula; it is needed for ordinary time-step distributions to converge to π rather than cycle among periodic classes.",
        """Equilibrium is not merely a vector fixed by a matrix. It is also a time-allocation law: states that recur quickly occupy more stationary mass.

The excursion viewpoint turns one infinite path into regenerative blocks and converts temporal frequency into a local return statistic. It also prevents a common hypothesis error. Uniqueness of the stationary distribution for a finite irreducible chain survives periodicity; convergence from an arbitrary start may not. Separating those conclusions is essential whenever “eventually stationary” is used, because algebraic invariance and dynamical mixing answer different questions.""",
        representations=["transition_operator", "excursions", "occupation_measure"],
        concepts=["stationarity", "return_time", "irreducibility"],
        moves=["decomposition", "change_of_representation", "prediction_falsification"],
        epistemic_role="existence_identity_with_hypothesis_boundary",
        geometry_role="meaningful_bridge",
        depth_contribution="time-domain interpretation of stationary measure with periodicity boundary",
    ),
    deep_unit(
        "sp_commute_resistance",
        "stochastic_processes",
        "mit_stochastic_processes_18_445_s15",
        "Electrical resistance computes random-walk commute time",
        "Course archive members static_resources/02c81e4fe01f0d97bb644c2d407d1a46_MIT18_445S15_lecture9.pdf and static_resources/1c4e0f0bf28f0ec9f0fd6bc8f7b896f1_MIT18_445S15_lecture10.pdf, electrical-network identities and the commute-time theorem",
        "Give each edge of a finite connected network a conductance and let the random walk move across adjacent edges with probability proportional to conductance. For vertices a and b, the expected time to hit b from a plus the expected time to return from b to a equals c_G R_eff(a↔b), where c_G is the total directed conductance normalization used in the notes and R_eff is effective electrical resistance. Voltage functions with boundary values at a and b are harmonic at all other vertices, just as hitting probabilities satisfy the mean-value equation for the walk. Currents encode expected edge traversals, and energy or voltage-drop identities yield the commute formula. The bridge is exact for the conductance-weighted reversible walk; changing transition probabilities independently of edge conductances destroys the electrical correspondence.",
        """Two stories share one harmonic equation. In the stochastic story, averaging expresses the next-step rule. In the electrical story, Kirchhoff’s law expresses conservation of current. Boundary values pin down the same unique function.

That shared operator lets probabilistic time be read through geometric resistance: bottlenecks raise both effective resistance and expected commute. But only the round trip is symmetric; one-way hitting times can be highly asymmetric even though resistance is symmetric. The representation therefore compresses a specific reversible combination of passage times, not the full directed dynamics of a Markov chain.""",
        representations=["random_walk", "electrical_network", "harmonic_function"],
        concepts=["hitting_time", "effective_resistance", "reversibility"],
        moves=["bridge_construction", "geometricization", "analogy_boundary"],
        epistemic_role="cross_representation_identity",
        geometry_role="primary",
        depth_contribution="exact stochastic-electrical bridge with a stated reversibility and symmetry boundary",
    ),
    deep_unit(
        "sp_optional_stopping_boundary",
        "stochastic_processes",
        "mit_stochastic_processes_18_445_s15",
        "Stopping a martingale preserves expectation only under control of the stop",
        "Course archive member static_resources/ddeda684b0dd6a1422418c7eca3ce843_MIT18_445S15_lecture16.pdf, Lecture 16, optional stopping theorem variants, hypotheses, and gambler’s-ruin application",
        "Let M_n be a martingale and T a stopping time. For a bounded stopping time, M_T has the same expectation as M_0: write M_T as a telescoping sum of increments multiplied by indicators of the events {T≥n}; those indicators are known before the nth increment, so every expected contribution is zero. The lecture extends the conclusion when the entire martingale is dominated by one integrable random variable and T is almost surely finite, or when T has finite expectation and the martingale has uniformly bounded increments. In gambler’s ruin, stopping a fair walk on first hitting either boundary is legitimate because the stopped position is bounded; expectation preservation then determines the hitting probability. Almost-sure finiteness by itself is not one of the stated sufficient conditions.",
        """Optional stopping is a conservation law with an interface contract. Adaptedness prevents the stopping rule from peeking into the future; integrability or boundedness prevents mass from escaping through extremely late outcomes.

A safe proof should name which contract is used, not invoke “fair game” intuition. First prove the bounded-time identity from predictable indicators. Then justify passage to the desired stopping time using the theorem’s domination condition or its finite-mean-time and bounded-increment condition. Almost-sure termination alone answers whether the game ends, not whether expectations commute with that random limit. The distinction is the probabilistic analogue of exchanging limits and integrals only after securing control.""",
        representations=["martingale", "stopping_time", "telescoping_increments"],
        concepts=["optional_stopping", "adaptedness", "dominated_convergence"],
        moves=["invariant_tracking", "counterfactual_reasoning", "prediction_falsification"],
        epistemic_role="theorem_and_failure_boundary",
        geometry_role="absent",
        depth_contribution="worked stopping theorem with proof mechanism and nonoptional hypotheses",
    ),
    deep_unit(
        "pde_maximum_comparison",
        "partial_differential_equations",
        "mit_pde_18_152_f11",
        "A spacetime maximum contradicts a strict heat inequality",
        "Course archive member static_resources/da093b7265d1fc4fe9c6edf3e7825661_MIT18_152F11_lec_04.pdf, Lecture 4, Theorem 1.1 and Corollary 1.0.1, weak maximum principle and comparison principle",
        "Let w solve the possibly inhomogeneous heat equation w_t−DΔw=f on a spacetime cylinder Q_T, with f nonpositive. The weak maximum principle says that w attains its maximum on the parabolic boundary: the initial time slice together with the spatial boundary, not the terminal time slice. The proof perturbs to u=w−εt, so u_t−DΔu is strictly negative. At a putative maximum away from the parabolic boundary, the time derivative is nonnegative and the spatial Hessian is negative semidefinite, making u_t−DΔu nonnegative, a contradiction. Letting ε decrease to zero yields the weak result. Applying it to differences of heat solutions gives comparison and a stability bound controlled by parabolic-boundary disagreement plus time times the maximum forcing disagreement.",
        """The theorem turns local differential information into global order. It does not solve the equation point by point; it rules out where an extremum capable of violating the desired comparison could hide.

This is why uniqueness can come before construction. If two candidate solutions share initial and spatial boundary data, their difference obeys the homogeneous heat equation and cannot develop a new positive or negative spacetime extremum. The mechanism depends on the forward time direction, positive diffusivity, regularity, and the parabolic boundary. An elliptic problem has a related but different boundary geometry, while a hyperbolic equation propagates information along characteristics. “Maximum principle” is therefore an operator-specific order mechanism, not one undifferentiated PDE slogan.""",
        representations=["parabolic_operator", "spacetime_extremum", "barrier"],
        concepts=["maximum_principle", "comparison", "uniqueness"],
        moves=["prediction_falsification", "local_global", "reframing"],
        epistemic_role="comparison_proof_and_consequence",
        geometry_role="primary",
        depth_contribution="PDE-specific local-to-global order mechanism yielding uniqueness without explicit solution",
    ),
    deep_unit(
        "pde_heat_kernel",
        "partial_differential_equations",
        "mit_pde_18_152_f11",
        "The heat kernel builds evolution by spreading every point source",
        "Course archive member static_resources/9acdeff6449529106ac254f7ada967da_MIT18_152F11_lec_05.pdf, Lecture 5, fundamental solution of the heat equation, delta limit, and convolution formula",
        "The Gaussian heat kernel Γ(x,t) for positive time solves the heat equation, has total mass one, and concentrates at the origin as t decreases to zero in the sense of the delta distribution. For suitable initial data g on Euclidean space, define u(x,t) by convolving g with Γ(·,t). Differentiation under the integral transfers the heat equation from Γ to u, while the delta-limit property recovers g as t approaches zero. Positivity and unit mass show that u(x,t) is a weighted average of initial values, explaining smoothing and compatibility with the maximum principle. The Gaussian’s spatial scale grows with positive time, spreading a point source across a wider region. This representation relies on linearity, translation invariance, and whole-space geometry; boundaries require modified kernels or other methods.",
        """A fundamental solution is a response dictionary. Solve the equation for one idealized point source, translate that response to every source location, and superpose with weights supplied by the initial data.

From the same formula one can read several consequences without re-solving the PDE: positivity preserves order, normalization preserves total mass, and Gaussian width records diffusion scale. The delta initial state is not an ordinary function, so recovery is a limiting statement. Nonlinear equations cannot generally use superposition, and bounded domains interrupt translation symmetry. The kernel method is powerful because its exact structural hypotheses are visible in the construction.""",
        representations=["fundamental_solution", "convolution", "Gaussian_scaling"],
        concepts=["heat_equation", "smoothing", "approximate_identity"],
        moves=["synthesis", "change_of_representation", "prediction_falsification"],
        epistemic_role="solution_construction_and_consequence",
        geometry_role="meaningful_bridge",
        depth_contribution="worked Green-kernel synthesis with reconstruction and domain boundaries",
    ),
    deep_unit(
        "pde_characteristics_shock",
        "partial_differential_equations",
        "mit_pde_18_152_f11",
        "Characteristics simplify transport until their crossing creates a shock",
        "Course archive member static_resources/29c6f7ee914a1d804899781f9f604f49_MIT18_152F11_lec_24.pdf, Lecture 24, method of characteristics for transport equations and finite-time shock formation for Burgers’ equation",
        "For a first-order transport equation, choose curves in spacetime whose velocity is the transport coefficient. Along each characteristic, the chain rule converts the PDE into an ordinary differential equation, often making the transported quantity constant. For inviscid Burgers’ equation u_t+u u_x=0, a characteristic starting at position ξ moves with speed equal to its initial value u_0(ξ), so x=ξ+t u_0(ξ) and u remains u_0(ξ) along the curve. If the initial profile decreases somewhere, faster characteristics from the left can overtake slower ones. The map from labels ξ to current positions then loses invertibility when 1+t u_0′(ξ)=0, and the classical derivative blows up. The equation may need a weak solution with a shock beyond that time, together with an additional admissibility condition.",
        """Characteristics are coordinates adapted to information flow. They remove a derivative by moving with the equation, but the coordinate change is only valid while different labels reach different spacetime points.

This yields a built-in forecast of singularity: monitor the Jacobian of the characteristic map. When it vanishes, the representation that made the PDE simple ceases to be one-to-one, even though each individual characteristic remains smooth. Shock formation is therefore not an unexplained failure of calculus; it is the geometric collision of transported states. Viscosity, higher dimensions, and weak-solution selection alter the continuation and cannot be inferred from the pre-shock picture alone.""",
        representations=["spacetime_characteristics", "Lagrangian_coordinates", "weak_solution"],
        concepts=["transport", "shock", "loss_of_invertibility"],
        moves=["geometricization", "simplification", "prediction_falsification"],
        epistemic_role="solution_method_and_breakdown",
        geometry_role="primary",
        depth_contribution="PDE representation whose precise geometric failure predicts singularity",
    ),
    deep_unit(
        "na_newton_quadratic",
        "numerical_analysis",
        "mit_numerical_methods_18_335j_s19",
        "Newton iteration squares small relative error near a simple root",
        "Course archive member static_resources/0a734ecc94b60a26213488e68588bc8d_MIT18_335JS19_lec1.pdf, Lecture 1, Babylonian square-root iteration, monotone convergence, and local quadratic error analysis",
        "For a positive target a, Newton’s method applied to x²−a gives x_{n+1}=(x_n+a/x_n)/2. Starting from a positive value above √a, the arithmetic-geometric mean inequality keeps the iterates above the root, while a direct comparison shows they decrease; bounded monotonicity therefore proves convergence, and the fixed-point equation identifies the limit as √a. Write x_n=√a(1+δ_n). Substitution gives an exact recurrence in δ_n whose leading term is δ_n²/2, so sufficiently small relative error is approximately squared at each step. The number of correct digits then roughly doubles per iteration. The local rate does not imply that arbitrary Newton iterations converge: other functions or starting points can encounter zero derivatives, cycles, or attraction to a different root.",
        """There are two proofs here, serving different questions. Monotone boundedness establishes that this particular iteration reaches the intended root from a controlled region. Error expansion explains how fast it approaches once close.

Conflating them is risky. A local quadratic formula gives no global basin of attraction, while a convergence proof without an error recurrence says little about computational efficiency. Newton’s method is best understood through both the geometry of the update and the dynamics of the error map. The simple-root hypothesis is load-bearing: at a multiple root, the leading error behavior usually drops to linear unless the method is modified.""",
        representations=["fixed_point_iteration", "relative_error", "local_dynamics"],
        concepts=["Newton_method", "quadratic_convergence", "basin_of_attraction"],
        moves=["exact_approximate", "linearization", "prediction_falsification"],
        epistemic_role="convergence_and_rate_proof",
        geometry_role="meaningful_bridge",
        depth_contribution="algorithm-scale separation of global convergence from local rate",
    ),
    deep_unit(
        "na_summation_condition",
        "numerical_analysis",
        "mit_numerical_methods_18_335j_s19",
        "A small rounding residual can become a large relative error through cancellation",
        "Course archive member static_resources/906cd44ea38d0bb54e13138efd67f3a1_MIT18_335JS19_lec3-1.pdf, Lecture 3a, floating-point model and forward-error analysis of naive summation",
        "In the standard floating-point model, each addition returns the exact sum multiplied by one plus a small relative perturbation. Expanding the recursive computation of a_1+⋯+a_n shows that each input is multiplied by a product of nearby perturbation factors. To first order, the absolute forward error is bounded by a modest multiple of machine precision times the sum of the absolute input magnitudes. Dividing by the magnitude of the exact sum introduces the condition factor (Σ|a_i|)/|Σa_i|. When terms largely cancel, this factor can be enormous even though every arithmetic step is accurate relative to its local result. Thus an observed large relative output error may reflect sensitivity of the summation problem for those data, accumulation by the algorithm, or both; the bound separates the local rounding model from the data-dependent amplification.",
        """“The computer made a large error” merges two questions. How much perturbation did the algorithm introduce? How strongly does the mathematical output react to such perturbations?

Naive summation supplies the cleanest separation. The arithmetic contributes a factor growing with the number of operations and machine precision. Cancellation contributes a condition factor determined before the algorithm is chosen. Rearrangement or compensated summation may reduce algorithmic accumulation, but it cannot make a nearly zero exact sum well conditioned under relative input perturbations. Reporting only relative forward error hides this distinction precisely when cancellation is strongest.""",
        representations=["floating_point_model", "forward_error_bound", "condition_factor"],
        concepts=["roundoff", "conditioning", "cancellation"],
        moves=["decomposition", "prediction_falsification", "perspective_selection"],
        epistemic_role="worked_error_bound",
        geometry_role="absent",
        depth_contribution="quantitative separation of problem sensitivity from arithmetic perturbation",
    ),
    deep_unit(
        "na_backward_stability",
        "numerical_analysis",
        "mit_numerical_methods_18_335j_s19",
        "Recursive summation is exact for nearby inputs",
        "Course archive member static_resources/ac7d12a336af115e9f4a57740021c8f0_MIT18_335JS19_lec3-2.pdf, Lecture 3b, backward stability analysis of recursive summation",
        "Let the recursively computed partial sums satisfy s̃_i=s̃_{i−1}⊕x_i. To interpret the final value backward, define nearby inputs x̃_i so that each floating-point update is exactly s̃_i=s̃_{i−1}+x̃_i. Induction then makes the computed output the exact mathematical sum of x̃. The rounding model expresses x̃_i−x_i through the local addition error and the preceding computed partial sum. Summing these perturbations and using the triangle inequality gives an L1 normwise bound ‖x̃−x‖₁=‖x‖₁O(ε_machine), with a constant that may depend on the fixed problem size. This proves normwise backward stability under the stated no-overflow/no-underflow model. It does not prove that each component has a small relative perturbation, nor does it promise small relative forward error when cancellation makes summation ill conditioned.",
        """Backward analysis changes the question from “how far is the answer from the original exact answer?” to “for what nearby problem is this answer exact?” That reframing often matches how roundoff actually propagates.

It is a certificate about the algorithm, not a universal certificate about the output. A backward-stable method applied to ill-conditioned data can return a forward-inaccurate result because all nearby problems disagree strongly. Conversely, a small forward error in one case does not establish algorithmic stability. The two notions compose: stability controls the effective input perturbation; conditioning controls how that perturbation moves the mathematical solution.""",
        representations=["perturbed_input", "exact_nearby_problem", "error_composition"],
        concepts=["backward_stability", "forward_error", "conditioning"],
        moves=["reframing", "exact_approximate", "synthesis"],
        epistemic_role="stability_certificate",
        geometry_role="absent",
        depth_contribution="worked nearby-problem interpretation separating algorithmic stability from solution accuracy",
    ),
]
