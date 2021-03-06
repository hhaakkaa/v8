# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  26: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  32: "STRING_TYPE",
  33: "CONS_STRING_TYPE",
  34: "EXTERNAL_STRING_TYPE",
  35: "SLICED_STRING_TYPE",
  37: "THIN_STRING_TYPE",
  40: "ONE_BYTE_STRING_TYPE",
  41: "CONS_ONE_BYTE_STRING_TYPE",
  42: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  43: "SLICED_ONE_BYTE_STRING_TYPE",
  45: "THIN_ONE_BYTE_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_STRING_TYPE",
  58: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  64: "SYMBOL_TYPE",
  65: "HEAP_NUMBER_TYPE",
  66: "BIGINT_TYPE",
  67: "ODDBALL_TYPE",
  68: "MAP_TYPE",
  69: "CODE_TYPE",
  70: "MUTABLE_HEAP_NUMBER_TYPE",
  71: "FOREIGN_TYPE",
  72: "BYTE_ARRAY_TYPE",
  73: "BYTECODE_ARRAY_TYPE",
  74: "FREE_SPACE_TYPE",
  75: "FIXED_INT8_ARRAY_TYPE",
  76: "FIXED_UINT8_ARRAY_TYPE",
  77: "FIXED_INT16_ARRAY_TYPE",
  78: "FIXED_UINT16_ARRAY_TYPE",
  79: "FIXED_INT32_ARRAY_TYPE",
  80: "FIXED_UINT32_ARRAY_TYPE",
  81: "FIXED_FLOAT32_ARRAY_TYPE",
  82: "FIXED_FLOAT64_ARRAY_TYPE",
  83: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  84: "FIXED_BIGINT64_ARRAY_TYPE",
  85: "FIXED_BIGUINT64_ARRAY_TYPE",
  86: "FIXED_DOUBLE_ARRAY_TYPE",
  87: "FEEDBACK_METADATA_TYPE",
  88: "FILLER_TYPE",
  89: "ACCESS_CHECK_INFO_TYPE",
  90: "ACCESSOR_INFO_TYPE",
  91: "ACCESSOR_PAIR_TYPE",
  92: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  93: "ALLOCATION_MEMENTO_TYPE",
  94: "ASM_WASM_DATA_TYPE",
  95: "ASYNC_GENERATOR_REQUEST_TYPE",
  96: "CLASS_POSITIONS_TYPE",
  97: "DEBUG_INFO_TYPE",
  98: "ENUM_CACHE_TYPE",
  99: "FUNCTION_TEMPLATE_INFO_TYPE",
  100: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  101: "INTERCEPTOR_INFO_TYPE",
  102: "INTERPRETER_DATA_TYPE",
  103: "MODULE_INFO_ENTRY_TYPE",
  104: "MODULE_TYPE",
  105: "OBJECT_TEMPLATE_INFO_TYPE",
  106: "PROMISE_CAPABILITY_TYPE",
  107: "PROMISE_REACTION_TYPE",
  108: "PROTOTYPE_INFO_TYPE",
  109: "SCRIPT_TYPE",
  110: "STACK_FRAME_INFO_TYPE",
  111: "STACK_TRACE_FRAME_TYPE",
  112: "TUPLE2_TYPE",
  113: "TUPLE3_TYPE",
  114: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  115: "WASM_DEBUG_INFO_TYPE",
  116: "WASM_EXCEPTION_TAG_TYPE",
  117: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  118: "CALLABLE_TASK_TYPE",
  119: "CALLBACK_TASK_TYPE",
  120: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  121: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  122: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  123: "FINALIZATION_GROUP_CLEANUP_JOB_TASK_TYPE",
  124: "ALLOCATION_SITE_TYPE",
  125: "EMBEDDER_DATA_ARRAY_TYPE",
  126: "FIXED_ARRAY_TYPE",
  127: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  128: "CLOSURE_FEEDBACK_CELL_ARRAY_TYPE",
  129: "HASH_TABLE_TYPE",
  130: "ORDERED_HASH_MAP_TYPE",
  131: "ORDERED_HASH_SET_TYPE",
  132: "ORDERED_NAME_DICTIONARY_TYPE",
  133: "NAME_DICTIONARY_TYPE",
  134: "GLOBAL_DICTIONARY_TYPE",
  135: "NUMBER_DICTIONARY_TYPE",
  136: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  137: "STRING_TABLE_TYPE",
  138: "EPHEMERON_HASH_TABLE_TYPE",
  139: "SCOPE_INFO_TYPE",
  140: "SCRIPT_CONTEXT_TABLE_TYPE",
  141: "AWAIT_CONTEXT_TYPE",
  142: "BLOCK_CONTEXT_TYPE",
  143: "CATCH_CONTEXT_TYPE",
  144: "DEBUG_EVALUATE_CONTEXT_TYPE",
  145: "EVAL_CONTEXT_TYPE",
  146: "FUNCTION_CONTEXT_TYPE",
  147: "MODULE_CONTEXT_TYPE",
  148: "NATIVE_CONTEXT_TYPE",
  149: "SCRIPT_CONTEXT_TYPE",
  150: "WITH_CONTEXT_TYPE",
  151: "WEAK_FIXED_ARRAY_TYPE",
  152: "TRANSITION_ARRAY_TYPE",
  153: "CALL_HANDLER_INFO_TYPE",
  154: "CELL_TYPE",
  155: "CODE_DATA_CONTAINER_TYPE",
  156: "DESCRIPTOR_ARRAY_TYPE",
  157: "FEEDBACK_CELL_TYPE",
  158: "FEEDBACK_VECTOR_TYPE",
  159: "LOAD_HANDLER_TYPE",
  160: "PREPARSE_DATA_TYPE",
  161: "PROPERTY_ARRAY_TYPE",
  162: "PROPERTY_CELL_TYPE",
  163: "SHARED_FUNCTION_INFO_TYPE",
  164: "SMALL_ORDERED_HASH_MAP_TYPE",
  165: "SMALL_ORDERED_HASH_SET_TYPE",
  166: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  167: "STORE_HANDLER_TYPE",
  168: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  169: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  170: "WEAK_ARRAY_LIST_TYPE",
  171: "WEAK_CELL_TYPE",
  1024: "JS_PROXY_TYPE",
  1025: "JS_GLOBAL_OBJECT_TYPE",
  1026: "JS_GLOBAL_PROXY_TYPE",
  1027: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_VALUE_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1057: "JS_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_TYPE",
  1059: "JS_ARRAY_BUFFER_TYPE",
  1060: "JS_ARRAY_ITERATOR_TYPE",
  1061: "JS_ARRAY_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  1064: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1065: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1066: "JS_DATE_TYPE",
  1067: "JS_ERROR_TYPE",
  1068: "JS_GENERATOR_OBJECT_TYPE",
  1069: "JS_MAP_TYPE",
  1070: "JS_MAP_KEY_ITERATOR_TYPE",
  1071: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1072: "JS_MAP_VALUE_ITERATOR_TYPE",
  1073: "JS_MESSAGE_OBJECT_TYPE",
  1074: "JS_PROMISE_TYPE",
  1075: "JS_REGEXP_TYPE",
  1076: "JS_REGEXP_STRING_ITERATOR_TYPE",
  1077: "JS_SET_TYPE",
  1078: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1079: "JS_SET_VALUE_ITERATOR_TYPE",
  1080: "JS_STRING_ITERATOR_TYPE",
  1081: "JS_WEAK_REF_TYPE",
  1082: "JS_FINALIZATION_GROUP_CLEANUP_ITERATOR_TYPE",
  1083: "JS_FINALIZATION_GROUP_TYPE",
  1084: "JS_WEAK_MAP_TYPE",
  1085: "JS_WEAK_SET_TYPE",
  1086: "JS_TYPED_ARRAY_TYPE",
  1087: "JS_DATA_VIEW_TYPE",
  1088: "JS_INTL_V8_BREAK_ITERATOR_TYPE",
  1089: "JS_INTL_COLLATOR_TYPE",
  1090: "JS_INTL_DATE_TIME_FORMAT_TYPE",
  1091: "JS_INTL_LIST_FORMAT_TYPE",
  1092: "JS_INTL_LOCALE_TYPE",
  1093: "JS_INTL_NUMBER_FORMAT_TYPE",
  1094: "JS_INTL_PLURAL_RULES_TYPE",
  1095: "JS_INTL_RELATIVE_TIME_FORMAT_TYPE",
  1096: "JS_INTL_SEGMENT_ITERATOR_TYPE",
  1097: "JS_INTL_SEGMENTER_TYPE",
  1098: "WASM_EXCEPTION_TYPE",
  1099: "WASM_GLOBAL_TYPE",
  1100: "WASM_INSTANCE_TYPE",
  1101: "WASM_MEMORY_TYPE",
  1102: "WASM_MODULE_TYPE",
  1103: "WASM_TABLE_TYPE",
  1104: "JS_BOUND_FUNCTION_TYPE",
  1105: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("read_only_space", 0x00139): (74, "FreeSpaceMap"),
  ("read_only_space", 0x00189): (68, "MetaMap"),
  ("read_only_space", 0x00209): (67, "NullMap"),
  ("read_only_space", 0x00271): (156, "DescriptorArrayMap"),
  ("read_only_space", 0x002d1): (151, "WeakFixedArrayMap"),
  ("read_only_space", 0x00321): (88, "OnePointerFillerMap"),
  ("read_only_space", 0x00371): (88, "TwoPointerFillerMap"),
  ("read_only_space", 0x003f1): (67, "UninitializedMap"),
  ("read_only_space", 0x00461): (8, "OneByteInternalizedStringMap"),
  ("read_only_space", 0x00501): (67, "UndefinedMap"),
  ("read_only_space", 0x00561): (65, "HeapNumberMap"),
  ("read_only_space", 0x005e1): (67, "TheHoleMap"),
  ("read_only_space", 0x00689): (67, "BooleanMap"),
  ("read_only_space", 0x00761): (72, "ByteArrayMap"),
  ("read_only_space", 0x007b1): (126, "FixedArrayMap"),
  ("read_only_space", 0x00801): (126, "FixedCOWArrayMap"),
  ("read_only_space", 0x00851): (129, "HashTableMap"),
  ("read_only_space", 0x008a1): (64, "SymbolMap"),
  ("read_only_space", 0x008f1): (40, "OneByteStringMap"),
  ("read_only_space", 0x00941): (139, "ScopeInfoMap"),
  ("read_only_space", 0x00991): (163, "SharedFunctionInfoMap"),
  ("read_only_space", 0x009e1): (69, "CodeMap"),
  ("read_only_space", 0x00a31): (146, "FunctionContextMap"),
  ("read_only_space", 0x00a81): (154, "CellMap"),
  ("read_only_space", 0x00ad1): (162, "GlobalPropertyCellMap"),
  ("read_only_space", 0x00b21): (71, "ForeignMap"),
  ("read_only_space", 0x00b71): (152, "TransitionArrayMap"),
  ("read_only_space", 0x00bc1): (158, "FeedbackVectorMap"),
  ("read_only_space", 0x00c61): (67, "ArgumentsMarkerMap"),
  ("read_only_space", 0x00d01): (67, "ExceptionMap"),
  ("read_only_space", 0x00da1): (67, "TerminationExceptionMap"),
  ("read_only_space", 0x00e49): (67, "OptimizedOutMap"),
  ("read_only_space", 0x00ee9): (67, "StaleRegisterMap"),
  ("read_only_space", 0x00f59): (148, "NativeContextMap"),
  ("read_only_space", 0x00fa9): (147, "ModuleContextMap"),
  ("read_only_space", 0x00ff9): (145, "EvalContextMap"),
  ("read_only_space", 0x01049): (149, "ScriptContextMap"),
  ("read_only_space", 0x01099): (141, "AwaitContextMap"),
  ("read_only_space", 0x010e9): (142, "BlockContextMap"),
  ("read_only_space", 0x01139): (143, "CatchContextMap"),
  ("read_only_space", 0x01189): (150, "WithContextMap"),
  ("read_only_space", 0x011d9): (144, "DebugEvaluateContextMap"),
  ("read_only_space", 0x01229): (140, "ScriptContextTableMap"),
  ("read_only_space", 0x01279): (128, "ClosureFeedbackCellArrayMap"),
  ("read_only_space", 0x012c9): (87, "FeedbackMetadataArrayMap"),
  ("read_only_space", 0x01319): (126, "ArrayListMap"),
  ("read_only_space", 0x01369): (66, "BigIntMap"),
  ("read_only_space", 0x013b9): (127, "ObjectBoilerplateDescriptionMap"),
  ("read_only_space", 0x01409): (73, "BytecodeArrayMap"),
  ("read_only_space", 0x01459): (155, "CodeDataContainerMap"),
  ("read_only_space", 0x014a9): (86, "FixedDoubleArrayMap"),
  ("read_only_space", 0x014f9): (134, "GlobalDictionaryMap"),
  ("read_only_space", 0x01549): (157, "ManyClosuresCellMap"),
  ("read_only_space", 0x01599): (126, "ModuleInfoMap"),
  ("read_only_space", 0x015e9): (70, "MutableHeapNumberMap"),
  ("read_only_space", 0x01639): (133, "NameDictionaryMap"),
  ("read_only_space", 0x01689): (157, "NoClosuresCellMap"),
  ("read_only_space", 0x016d9): (135, "NumberDictionaryMap"),
  ("read_only_space", 0x01729): (157, "OneClosureCellMap"),
  ("read_only_space", 0x01779): (130, "OrderedHashMapMap"),
  ("read_only_space", 0x017c9): (131, "OrderedHashSetMap"),
  ("read_only_space", 0x01819): (132, "OrderedNameDictionaryMap"),
  ("read_only_space", 0x01869): (160, "PreparseDataMap"),
  ("read_only_space", 0x018b9): (161, "PropertyArrayMap"),
  ("read_only_space", 0x01909): (153, "SideEffectCallHandlerInfoMap"),
  ("read_only_space", 0x01959): (153, "SideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x019a9): (153, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x019f9): (136, "SimpleNumberDictionaryMap"),
  ("read_only_space", 0x01a49): (126, "SloppyArgumentsElementsMap"),
  ("read_only_space", 0x01a99): (164, "SmallOrderedHashMapMap"),
  ("read_only_space", 0x01ae9): (165, "SmallOrderedHashSetMap"),
  ("read_only_space", 0x01b39): (166, "SmallOrderedNameDictionaryMap"),
  ("read_only_space", 0x01b89): (137, "StringTableMap"),
  ("read_only_space", 0x01bd9): (168, "UncompiledDataWithoutPreparseDataMap"),
  ("read_only_space", 0x01c29): (169, "UncompiledDataWithPreparseDataMap"),
  ("read_only_space", 0x01c79): (170, "WeakArrayListMap"),
  ("read_only_space", 0x01cc9): (138, "EphemeronHashTableMap"),
  ("read_only_space", 0x01d19): (125, "EmbedderDataArrayMap"),
  ("read_only_space", 0x01d69): (171, "WeakCellMap"),
  ("read_only_space", 0x01db9): (58, "NativeSourceStringMap"),
  ("read_only_space", 0x01e09): (32, "StringMap"),
  ("read_only_space", 0x01e59): (41, "ConsOneByteStringMap"),
  ("read_only_space", 0x01ea9): (33, "ConsStringMap"),
  ("read_only_space", 0x01ef9): (45, "ThinOneByteStringMap"),
  ("read_only_space", 0x01f49): (37, "ThinStringMap"),
  ("read_only_space", 0x01f99): (35, "SlicedStringMap"),
  ("read_only_space", 0x01fe9): (43, "SlicedOneByteStringMap"),
  ("read_only_space", 0x02039): (34, "ExternalStringMap"),
  ("read_only_space", 0x02089): (42, "ExternalOneByteStringMap"),
  ("read_only_space", 0x020d9): (50, "UncachedExternalStringMap"),
  ("read_only_space", 0x02129): (0, "InternalizedStringMap"),
  ("read_only_space", 0x02179): (2, "ExternalInternalizedStringMap"),
  ("read_only_space", 0x021c9): (10, "ExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x02219): (18, "UncachedExternalInternalizedStringMap"),
  ("read_only_space", 0x02269): (26, "UncachedExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x022b9): (58, "UncachedExternalOneByteStringMap"),
  ("read_only_space", 0x02309): (76, "FixedUint8ArrayMap"),
  ("read_only_space", 0x02359): (75, "FixedInt8ArrayMap"),
  ("read_only_space", 0x023a9): (78, "FixedUint16ArrayMap"),
  ("read_only_space", 0x023f9): (77, "FixedInt16ArrayMap"),
  ("read_only_space", 0x02449): (80, "FixedUint32ArrayMap"),
  ("read_only_space", 0x02499): (79, "FixedInt32ArrayMap"),
  ("read_only_space", 0x024e9): (81, "FixedFloat32ArrayMap"),
  ("read_only_space", 0x02539): (82, "FixedFloat64ArrayMap"),
  ("read_only_space", 0x02589): (83, "FixedUint8ClampedArrayMap"),
  ("read_only_space", 0x025d9): (85, "FixedBigUint64ArrayMap"),
  ("read_only_space", 0x02629): (84, "FixedBigInt64ArrayMap"),
  ("read_only_space", 0x02679): (67, "SelfReferenceMarkerMap"),
  ("read_only_space", 0x026e1): (98, "EnumCacheMap"),
  ("read_only_space", 0x02781): (114, "ArrayBoilerplateDescriptionMap"),
  ("read_only_space", 0x02ad1): (101, "InterceptorInfoMap"),
  ("read_only_space", 0x05109): (89, "AccessCheckInfoMap"),
  ("read_only_space", 0x05159): (90, "AccessorInfoMap"),
  ("read_only_space", 0x051a9): (91, "AccessorPairMap"),
  ("read_only_space", 0x051f9): (92, "AliasedArgumentsEntryMap"),
  ("read_only_space", 0x05249): (93, "AllocationMementoMap"),
  ("read_only_space", 0x05299): (94, "AsmWasmDataMap"),
  ("read_only_space", 0x052e9): (95, "AsyncGeneratorRequestMap"),
  ("read_only_space", 0x05339): (96, "ClassPositionsMap"),
  ("read_only_space", 0x05389): (97, "DebugInfoMap"),
  ("read_only_space", 0x053d9): (99, "FunctionTemplateInfoMap"),
  ("read_only_space", 0x05429): (100, "FunctionTemplateRareDataMap"),
  ("read_only_space", 0x05479): (102, "InterpreterDataMap"),
  ("read_only_space", 0x054c9): (103, "ModuleInfoEntryMap"),
  ("read_only_space", 0x05519): (104, "ModuleMap"),
  ("read_only_space", 0x05569): (105, "ObjectTemplateInfoMap"),
  ("read_only_space", 0x055b9): (106, "PromiseCapabilityMap"),
  ("read_only_space", 0x05609): (107, "PromiseReactionMap"),
  ("read_only_space", 0x05659): (108, "PrototypeInfoMap"),
  ("read_only_space", 0x056a9): (109, "ScriptMap"),
  ("read_only_space", 0x056f9): (110, "StackFrameInfoMap"),
  ("read_only_space", 0x05749): (111, "StackTraceFrameMap"),
  ("read_only_space", 0x05799): (112, "Tuple2Map"),
  ("read_only_space", 0x057e9): (113, "Tuple3Map"),
  ("read_only_space", 0x05839): (115, "WasmDebugInfoMap"),
  ("read_only_space", 0x05889): (116, "WasmExceptionTagMap"),
  ("read_only_space", 0x058d9): (117, "WasmExportedFunctionDataMap"),
  ("read_only_space", 0x05929): (118, "CallableTaskMap"),
  ("read_only_space", 0x05979): (119, "CallbackTaskMap"),
  ("read_only_space", 0x059c9): (120, "PromiseFulfillReactionJobTaskMap"),
  ("read_only_space", 0x05a19): (121, "PromiseRejectReactionJobTaskMap"),
  ("read_only_space", 0x05a69): (122, "PromiseResolveThenableJobTaskMap"),
  ("read_only_space", 0x05ab9): (123, "FinalizationGroupCleanupJobTaskMap"),
  ("read_only_space", 0x05b09): (124, "AllocationSiteWithWeakNextMap"),
  ("read_only_space", 0x05b59): (124, "AllocationSiteWithoutWeakNextMap"),
  ("read_only_space", 0x05ba9): (159, "LoadHandler1Map"),
  ("read_only_space", 0x05bf9): (159, "LoadHandler2Map"),
  ("read_only_space", 0x05c49): (159, "LoadHandler3Map"),
  ("read_only_space", 0x05c99): (167, "StoreHandler0Map"),
  ("read_only_space", 0x05ce9): (167, "StoreHandler1Map"),
  ("read_only_space", 0x05d39): (167, "StoreHandler2Map"),
  ("read_only_space", 0x05d89): (167, "StoreHandler3Map"),
  ("map_space", 0x00139): (1057, "ExternalMap"),
  ("map_space", 0x00189): (1073, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("read_only_space", 0x001d9): "NullValue",
  ("read_only_space", 0x00259): "EmptyDescriptorArray",
  ("read_only_space", 0x002c1): "EmptyWeakFixedArray",
  ("read_only_space", 0x003c1): "UninitializedValue",
  ("read_only_space", 0x004d1): "UndefinedValue",
  ("read_only_space", 0x00551): "NanValue",
  ("read_only_space", 0x005b1): "TheHoleValue",
  ("read_only_space", 0x00649): "HoleNanValue",
  ("read_only_space", 0x00659): "TrueValue",
  ("read_only_space", 0x00709): "FalseValue",
  ("read_only_space", 0x00751): "empty_string",
  ("read_only_space", 0x00c11): "EmptyScopeInfo",
  ("read_only_space", 0x00c21): "EmptyFixedArray",
  ("read_only_space", 0x00c31): "ArgumentsMarker",
  ("read_only_space", 0x00cd1): "Exception",
  ("read_only_space", 0x00d71): "TerminationException",
  ("read_only_space", 0x00e19): "OptimizedOut",
  ("read_only_space", 0x00eb9): "StaleRegister",
  ("read_only_space", 0x026c9): "EmptyEnumCache",
  ("read_only_space", 0x02731): "EmptyPropertyArray",
  ("read_only_space", 0x02741): "EmptyByteArray",
  ("read_only_space", 0x02751): "EmptyObjectBoilerplateDescription",
  ("read_only_space", 0x02769): "EmptyArrayBoilerplateDescription",
  ("read_only_space", 0x027d1): "EmptyClosureFeedbackCellArray",
  ("read_only_space", 0x027e1): "EmptyFixedUint8Array",
  ("read_only_space", 0x02801): "EmptyFixedInt8Array",
  ("read_only_space", 0x02821): "EmptyFixedUint16Array",
  ("read_only_space", 0x02841): "EmptyFixedInt16Array",
  ("read_only_space", 0x02861): "EmptyFixedUint32Array",
  ("read_only_space", 0x02881): "EmptyFixedInt32Array",
  ("read_only_space", 0x028a1): "EmptyFixedFloat32Array",
  ("read_only_space", 0x028c1): "EmptyFixedFloat64Array",
  ("read_only_space", 0x028e1): "EmptyFixedUint8ClampedArray",
  ("read_only_space", 0x02901): "EmptyFixedBigUint64Array",
  ("read_only_space", 0x02921): "EmptyFixedBigInt64Array",
  ("read_only_space", 0x02941): "EmptySloppyArgumentsElements",
  ("read_only_space", 0x02961): "EmptySlowElementDictionary",
  ("read_only_space", 0x029a9): "EmptyOrderedHashMap",
  ("read_only_space", 0x029d1): "EmptyOrderedHashSet",
  ("read_only_space", 0x029f9): "EmptyFeedbackMetadata",
  ("read_only_space", 0x02a09): "EmptyPropertyCell",
  ("read_only_space", 0x02a31): "EmptyPropertyDictionary",
  ("read_only_space", 0x02a81): "NoOpInterceptorInfo",
  ("read_only_space", 0x02b21): "EmptyWeakArrayList",
  ("read_only_space", 0x02b39): "InfinityValue",
  ("read_only_space", 0x02b49): "MinusZeroValue",
  ("read_only_space", 0x02b59): "MinusInfinityValue",
  ("read_only_space", 0x02b69): "SelfReferenceMarker",
  ("read_only_space", 0x02bc1): "OffHeapTrampolineRelocationInfo",
  ("read_only_space", 0x02bd9): "HashSeed",
  ("old_space", 0x00139): "ArgumentsIteratorAccessor",
  ("old_space", 0x001a9): "ArrayLengthAccessor",
  ("old_space", 0x00219): "BoundFunctionLengthAccessor",
  ("old_space", 0x00289): "BoundFunctionNameAccessor",
  ("old_space", 0x002f9): "ErrorStackAccessor",
  ("old_space", 0x00369): "FunctionArgumentsAccessor",
  ("old_space", 0x003d9): "FunctionCallerAccessor",
  ("old_space", 0x00449): "FunctionNameAccessor",
  ("old_space", 0x004b9): "FunctionLengthAccessor",
  ("old_space", 0x00529): "FunctionPrototypeAccessor",
  ("old_space", 0x00599): "StringLengthAccessor",
  ("old_space", 0x00609): "InvalidPrototypeValidityCell",
  ("old_space", 0x00619): "EmptyScript",
  ("old_space", 0x00699): "ManyClosuresCell",
  ("old_space", 0x006b1): "ArrayConstructorProtector",
  ("old_space", 0x006c1): "NoElementsProtector",
  ("old_space", 0x006e9): "IsConcatSpreadableProtector",
  ("old_space", 0x006f9): "ArraySpeciesProtector",
  ("old_space", 0x00721): "TypedArraySpeciesProtector",
  ("old_space", 0x00749): "RegExpSpeciesProtector",
  ("old_space", 0x00771): "PromiseSpeciesProtector",
  ("old_space", 0x00799): "StringLengthProtector",
  ("old_space", 0x007a9): "ArrayIteratorProtector",
  ("old_space", 0x007d1): "ArrayBufferDetachingProtector",
  ("old_space", 0x007f9): "PromiseHookProtector",
  ("old_space", 0x00821): "PromiseResolveProtector",
  ("old_space", 0x00831): "MapIteratorProtector",
  ("old_space", 0x00859): "PromiseThenProtector",
  ("old_space", 0x00881): "SetIteratorProtector",
  ("old_space", 0x008a9): "StringIteratorProtector",
  ("old_space", 0x008d1): "SingleCharacterStringCache",
  ("old_space", 0x010e1): "StringSplitCache",
  ("old_space", 0x018f1): "RegExpMultipleCache",
  ("old_space", 0x02101): "BuiltinsConstantsTable",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
